document.addEventListener("DOMContentLoaded", function () {
  if (typeof gsap !== "undefined" && typeof ScrollTrigger !== "undefined") {
    gsap.registerPlugin(ScrollTrigger);

    // 1. Aparición inicial en cascada
    const masterTimeline = gsap.timeline({
      scrollTrigger: {
        trigger: ".timeline-container",
        start: "top 85%",
        toggleActions: "play none none none"
      }
    });

    masterTimeline.to(".timeline-item", {
      opacity: 1,
      y: 0,
      duration: 0.7,
      stagger: 0.2,
      ease: "power3.out"
    });

    // 2. Animación interactiva por clic en el nodo (Ancho: 670px, Estado Sostenido)
    const nodes = document.querySelectorAll(".timeline-node");

    nodes.forEach(node => {
      const targetCardId = node.getAttribute("data-target");
      const card = document.getElementById(targetCardId);
      const frontContent = card.querySelector(".card-front-content");
      const detailsContent = card.querySelector(".card-details");

      const hoverTl = gsap.timeline({ paused: true });

      hoverTl.to(card, {
        zIndex: 100,
        rotation: 360,
        x: 140,
        duration: 0.6,
        ease: "power2.inOut"
      })
      .to(frontContent, { opacity: 0, duration: 0.1 }, "-=0.3")
      .to(card, {
        width: 670,
        height: 220,
        duration: 0.4,
        ease: "power2.out"
      })
      .to(detailsContent, {
        opacity: 1,
        pointerEvents: "auto",
        duration: 0.3
      });

      let isOpen = false;

      // Evento de clic en el nodo para alternar el estado y mantenerlo abierto
      node.addEventListener("click", (e) => {
        e.stopPropagation();
        isOpen = !isOpen;
        if (isOpen) {
          node.classList.add("active-node");
          hoverTl.play();
        } else {
          node.classList.remove("active-node");
          hoverTl.reverse();
        }
      });

      // Cerrar si se hace clic fuera de la tarjeta o del nodo activo
      document.addEventListener("click", (e) => {
        if (isOpen && !card.contains(e.target) && !node.contains(e.target)) {
          isOpen = false;
          node.classList.remove("active-node");
          hoverTl.reverse();
        }
      });
    });

  } else {
    document.querySelectorAll(".timeline-item").forEach(item => {
      item.style.opacity = 1;
      item.style.transform = "translateY(0)";
    });
  }
});
