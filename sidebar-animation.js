(function() {
    // 1. Configuración del elemento canvas en la barra lateral
    const sidebar = document.querySelector('.sidebar');
    if (!sidebar) return;

    sidebar.style.position = 'relative';
    sidebar.style.overflow = 'hidden';

    const canvas = document.createElement('canvas');
    canvas.id = 'sidebar-road-canvas';
    canvas.style.position = 'absolute';
    canvas.style.top = '0';
    canvas.style.left = '0';
    canvas.style.width = '100%';
    canvas.style.height = '100%';
    canvas.style.zIndex = '0';
    canvas.style.pointerEvents = 'none';

    sidebar.insertBefore(canvas, sidebar.firstChild);

    const children = sidebar.querySelectorAll('.profile-info, .contact-info');
    children.forEach(child => {
        child.style.position = 'relative';
        child.style.zIndex = '1';
    });

    const ctx = canvas.getContext('2d');

    function resizeCanvas() {
        canvas.width = sidebar.clientWidth;
        canvas.height = sidebar.clientHeight;
    }
    resizeCanvas();
    window.addEventListener('resize', resizeCanvas);

    // 2. Variables de estado de la animación
    let state = 'GENERATING'; // GENERATING, DRIVING, STOPPED, FADING
    let path = [];
    let totalPathLength = 0;
    let segmentLengths = [];
    
    // Configuración de los 3 vehículos en caravana
    let carProgresses = [0, -0.07, -0.14];
    let fadeAlpha = 1.0;
    
    // Semáforo
    let hasTrafficLight = false;
    let trafficLightPos = { x: 0, y: 0 };
    let trafficLightActive = false; // true cuando está en rojo (detenido)
    let trafficLightTriggered = false;

    function getRandomEdgePoint(w, h) {
        const edge = Math.floor(Math.random() * 4);
        switch(edge) {
            case 0: return { x: Math.random() * w, y: 0 };       // Arriba
            case 1: return { x: w, y: Math.random() * h };       // Derecha
            case 2: return { x: Math.random() * w, y: h };       // Abajo
            case 3: return { x: 0, y: Math.random() * h };       // Izquierda
        }
    }

    function calculatePathLength() {
        totalPathLength = 0;
        segmentLengths = [];
        for (let i = 0; i < path.length - 1; i++) {
            let p1 = path[i];
            let p2 = path[i+1];
            let dist = Math.hypot(p2.x - p1.x, p2.y - p1.y);
            segmentLengths.push(dist);
            totalPathLength += dist;
        }
    }

    function getPointAndTangentAtDistance(d) {
        if (d <= 0) return { pos: path[0], angle: 0 };
        if (d >= totalPathLength) return { pos: path[path.length - 1], angle: 0 };

        let accumulated = 0;
        for (let i = 0; i < segmentLengths.length; i++) {
            if (accumulated + segmentLengths[i] >= d) {
                let localD = d - accumulated;
                let t = localD / segmentLengths[i];
                let p1 = path[i];
                let p2 = path[i+1];
                let angle = Math.atan2(p2.y - p1.y, p2.x - p1.x);
                return {
                    pos: {
                        x: p1.x + (p2.x - p1.x) * t,
                        y: p1.y + (p2.y - p1.y) * t
                    },
                    angle: angle
                };
            }
            accumulated += segmentLengths[i];
        }
        return { pos: path[path.length - 1], angle: 0 };
    }

    function startNewPath() {
        let validPath = false;
        let attempts = 0;

        while (!validPath && attempts < 50) {
            attempts++;
            path = [];
            let start = getRandomEdgePoint(canvas.width, canvas.height);
            path.push(start);

            let current = { ...start };
            let steps = 6 + Math.floor(Math.random() * 5);
            let stepSize = 45;

            let dirX = 0, dirY = 0;
            if (current.y === 0) dirY = 1;
            else if (current.y === canvas.height) dirY = -1;
            else if (current.x === 0) dirX = 1;
            else if (current.x === canvas.width) dirX = -1;

            let hitEdge = false;

            for (let i = 0; i < steps; i++) {
                current.x += dirX * stepSize;
                current.y += dirY * stepSize;

                if (current.x <= 0 || current.x >= canvas.width || current.y <= 0 || current.y >= canvas.height) {
                    current.x = Math.max(0, Math.min(canvas.width, current.x));
                    current.y = Math.max(0, Math.min(canvas.height, current.y));
                    path.push({ ...current });
                    hitEdge = true;
                    break;
                }

                path.push({ ...current });

                if (Math.random() > 0.4) {
                    let temp = dirX;
                    dirX = -dirY;
                    dirY = temp;
                }
            }

            calculatePathLength();

            if (totalPathLength >= 560 && (hitEdge || path.length > 3)) {
                validPath = true;
            }
        }

        carProgresses = [0, -0.07, -0.14];
        hasTrafficLight = Math.random() > 0.5;
        trafficLightActive = false;
        trafficLightTriggered = false;

        if (hasTrafficLight) {
            // Calcular punto medio y desplazarlo lateralmente (fuera de las líneas de la vía)
            let midData = getPointAndTangentAtDistance(totalPathLength * 0.5);
            let sideOffset = 18; // Distancia lateral para que quede al lado de la vía
            let normalAngle = midData.angle + Math.PI / 2;
            
            trafficLightPos = {
                x: midData.pos.x + Math.cos(normalAngle) * sideOffset,
                y: midData.pos.y + Math.sin(normalAngle) * sideOffset
            };
        }

        state = 'DRIVING';
    }

    function animate() {
        ctx.clearRect(0, 0, canvas.width, canvas.height);

        if (state === 'GENERATING') {
            startNewPath();
        } 
        else if (state === 'DRIVING' || state === 'STOPPED') {
            // Dibujar la vía
            ctx.strokeStyle = `rgba(255, 255, 255, ${fadeAlpha * 0.2})`;
            ctx.lineWidth = 12;
            ctx.lineCap = 'round';
            ctx.lineJoin = 'round';

            ctx.beginPath();
            ctx.moveTo(path[0].x, path[0].y);
            for (let i = 1; i < path.length; i++) {
                ctx.lineTo(path[i].x, path[i].y);
            }
            ctx.stroke();

            // Activar semáforo al llegar al punto medio
            if (hasTrafficLight && !trafficLightTriggered && state === 'DRIVING') {
                if (carProgresses[0] >= 0.48) {
                    trafficLightTriggered = true;
                    trafficLightActive = true;
                    state = 'STOPPED';

                    // Programar la reanudación exacta tras 2 segundos de forma limpia
                    setTimeout(() => {
                        trafficLightActive = false;
                        if (state === 'STOPPED') {
                            state = 'DRIVING';
                        }
                    }, 2000);
                }
            }

            // Mover carros solo si no está detenido
            if (state === 'DRIVING') {
                let speed = 1.2 / totalPathLength;
                for (let i = 0; i < carProgresses.length; i++) {
                    carProgresses[i] += speed;
                }
            }

            // Dibujar el semáforo a un lado
            if (hasTrafficLight) {
                ctx.beginPath();
                ctx.arc(trafficLightPos.x, trafficLightPos.y, 7, 0, Math.PI * 2);
                ctx.strokeStyle = `rgba(255, 255, 255, ${fadeAlpha})`;
                ctx.lineWidth = 2;
                ctx.stroke();

                if (trafficLightActive) {
                    ctx.fillStyle = `rgba(255, 255, 255, ${fadeAlpha})`;
                    ctx.fill();
                }
            }

            // Dibujar los 3 carros en caravana
            for (let i = 0; i < carProgresses.length; i++) {
                let p = carProgresses[i];
                if (p >= 0 && p <= 1) {
                    let pointData = getPointAndTangentAtDistance(p * totalPathLength);
                    ctx.fillStyle = `rgba(255, 255, 255, ${fadeAlpha})`;
                    ctx.fillRect(pointData.pos.x - 4, pointData.pos.y - 4, 8, 8);
                }
            }

            if (carProgresses[0] > 1.05) {
                state = 'FADING';
            }
        } 
        else if (state === 'FADING') {
            ctx.strokeStyle = `rgba(255, 255, 255, ${fadeAlpha * 0.2})`;
            ctx.lineWidth = 12;
            ctx.lineCap = 'round';
            ctx.lineJoin = 'round';

            ctx.beginPath();
            ctx.moveTo(path[0].x, path[0].y);
            for (let i = 1; i < path.length; i++) {
                ctx.lineTo(path[i].x, path[i].y);
            }
            ctx.stroke();

            fadeAlpha -= 0.03;
            if (fadeAlpha <= 0) {
                fadeAlpha = 1.0;
                state = 'GENERATING';
            }
        }

        requestAnimationFrame(animate);
    }

    animate();
})();