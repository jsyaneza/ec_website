<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Juan Sebastián Yáñez Albarracín - Portafolio Académico</title>
  <style>
    /* Estilos Generales */
    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }
    body {
      font-family: 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
      display: flex;
      min-height: 100vh;
      background-color: #f4f6f9;
      color: #333;
    }

    /* Columna Izquierda: Barra Lateral */
    .sidebar {
      width: 320px;
      background-color: #1e293b;
      color: #ecf0f1;
      padding: 30px 20px;
      display: flex;
      flex-direction: column;
      flex-shrink: 0;
    }
    .profile-info {
      text-align: center;
      margin-bottom: 30px;
      padding-bottom: 20px;
      border-bottom: 1px solid #334155;
    }
    .profile-info h1 {
      font-size: 1.35rem;
      color: #ffffff;
      margin-bottom: 8px;
    }
    .profile-info h2 {
      font-size: 0.9rem;
      font-weight: 400;
      color: #38bdf8;
      margin-bottom: 15px;
    }
    .univ-details {
      font-size: 0.85rem;
      line-height: 1.5;
      color: #94a3b8;
      text-align: left;
      background-color: #0f172a;
      padding: 15px;
      border-radius: 8px;
    }
    .univ-details strong {
      color: #f1f5f9;
    }

    .contact-info {
      margin-top: auto;
      font-size: 0.85rem;
      color: #94a3b8;
      border-top: 1px solid #334155;
      padding-top: 20px;
    }
    .contact-info p {
      margin-bottom: 8px;
    }

    /* Columna Derecha: Contenido Principal */
    .main-content {
      flex-grow: 1;
      display: flex;
      flex-direction: column;
    }

    /* Menú de Navegación */
    .nav-tabs {
      display: flex;
      background-color: #ffffff;
      border-bottom: 2px solid #e2e8f0;
      box-shadow: 0 2px 4px rgba(0,0,0,0.02);
    }
    .tab-btn {
      padding: 18px 25px;
      border: none;
      background: none;
      font-size: 1rem;
      font-weight: 600;
      color: #64748b;
      cursor: pointer;
      transition: all 0.3s ease;
      border-bottom: 3px solid transparent;
    }
    .tab-btn:hover {
      color: #0284c7;
      background-color: #f8fafc;
    }
    .tab-btn.active {
      color: #0284c7;
      border-bottom-color: #0284c7;
      background-color: #ffffff;
    }

    /* Contenido de Secciones */
    .tab-content {
      display: none;
      padding: 40px;
      max-width: 900px;
    }
    .tab-content.active {
      display: block;
    }

    h2.section-title {
      font-size: 1.8rem;
      color: #0f172a;
      margin-bottom: 20px;
      border-bottom: 2px solid #0284c7;
      padding-bottom: 8px;
      display: inline-block;
    }
    h3 {
      font-size: 1.15rem;
      color: #1e293b;
      margin-top: 15px;
      margin-bottom: 10px;
    }
    p {
      line-height: 1.6;
      margin-bottom: 15px;
      color: #334155;
    }
    ul {
      margin-left: 20px;
      margin-bottom: 15px;
      line-height: 1.6;
      color: #334155;
    }
    li {
      margin-bottom: 6px;
    }

    .card {
      background: #ffffff;
      padding: 25px;
      border-radius: 8px;
      box-shadow: 0 1px 3px rgba(0,0,0,0.1);
      margin-bottom: 20px;
      border-left: 4px solid #0284c7;
    }

    /* Grid para Habilidades */
    .skills-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
      gap: 12px;
      margin-top: 15px;
    }
    .skill-item {
      background: #f1f5f9;
      padding: 12px;
      border-radius: 6px;
      font-size: 0.9rem;
    }
    .skill-item strong {
      display: block;
      color: #0f172a;
      margin-bottom: 4px;
    }

    /* Diseño Adaptable */
    @media (max-width: 850px) {
      body {
        flex-direction: column;
      }
      .sidebar {
        width: 100%;
      }
      .nav-tabs {
        flex-wrap: wrap;
      }
      .tab-btn {
        flex: 1;
        text-align: center;
        padding: 12px;
      }
    }
  </style>
</head>
<body>

  <!-- COLUMNA IZQUIERDA -->
  <aside class="sidebar">
    <div class="profile-info">
      <h1>JUAN SEBASTIÁN YAÑEZ ALBARRACÍN</h1>
      <h2>Visual Artist · Biologist · Researcher</h2>
      
      <div class="univ-details">
        <p><strong>Universidad:</strong> Nagoya University</p>
        <p><strong>Escuela:</strong> Graduate School of International Development (GSID)</p>
        <p><strong>Supervisión:</strong> Prof. Carlos Méndez</p>
        <p><strong>Línea:</strong> Econometría Regional, Desarrollo Espacial y Geografía Económica Cuantitativa</p>
      </div>
    </div>

    <div class="contact-info">
      <p><strong>Contacto:</strong></p>
      <p>Email: jsyaneza@unal.edu.co</p>
      <p>Ubicación: Bogotá DC, Colombia</p>
      <p>Teléfono: +57 (316) 520 8921</p>
    </div>
  </aside>

  <!-- COLUMNA DERECHA -->
  <main class="main-content">
    
    <!-- Menú -->
    <nav class="nav-tabs">
      <button class="tab-btn active" onclick="switchTab(event, 'intereses')">Intereses de Investigación</button>
      <button class="tab-btn" onclick="switchTab(event, 'cv')">Curriculum Vitae</button>
      <button class="tab-btn" onclick="switchTab(event, 'proyectos')">Proyectos</button>
    </nav>

    <!-- PÁGINA 1: Intereses -->
    <section id="intereses" class="tab-content active">
      <h2 class="section-title">Intereses de Investigación</h2>
      
      <div class="card">
        <h3>Enfoque y Propósito Académico</h3>
        <p>
          Mi motivación académica surge del interés por comprender cómo las personas interactúan con su entorno y cómo las decisiones sistémicas moldean las oportunidades de desarrollo. Tras doce años de experiencia gestionando una empresa en el sector alimentario, experimenté a escala micro las consecuencias de las políticas públicas, las fluctuaciones del mercado y las brechas de productividad regional.
        </p>
        <p>
          Mi objetivo de investigación es utilizar herramientas técnicas y econométricas para analizar dinámicas territoriales, modelar interacciones regionales y proponer recomendaciones de política pública basadas en evidencia.
        </p>
      </div>

      <div class="card">
        <h3>Líneas de Interés Principal</h3>
        <ul>
          <li><strong>Econometría Regional y Geografía Económica Cuantitativa:</strong> Análisis de las brechas de productividad entre departamentos y municipios de Colombia.</li>
          <li><strong>Análisis Espacial y Redes de Transporte:</strong> Evaluación del impacto de la geografía, infraestructura vial y efectos de aglomeración en las dinámicas socioeconómicas.</li>
          <li><strong>Evaluación Cuantitativa y Economía del Desarrollo:</strong> Modelado cuantitativo e intersectorial de heterogeneidades regionales y desigualdades territoriales.</li>
        </ul>
      </div>
    </section>

    <!-- PÁGINA 2: CV -->
    <section id="cv" class="tab-content">
      <h2 class="section-title">Curriculum Vitae</h2>

      <div class="card">
        <h3>Perfil</h3>
        <p>
          Artista visual y biólogo con sólida experiencia empresarial en el sector alimentario como CFO y Gerente de Desarrollo de Negocios en la startup UNOSEIS18. Experiencia combinada en análisis cuantitativo, finanzas, estrategia de mercado y solución de problemas del mundo real.
        </p>
      </div>

      <div class="card">
        <h3>Educación</h3>
        <ul>
          <li><strong>Pregrado en Biología:</strong> Universidad Nacional de Colombia - Bogotá (Ago 2009 – Abr 2018)</li>
          <li><strong>Pregrado en Artes Plásticas y Visuales:</strong> Universidad Distrital Francisco José de Caldas - Bogotá (Feb 2005 – Dic 2011) — <em>Mención meritoria por el trabajo de grado "Frío sólido"</em></li>
          <li><strong>Bachillerato:</strong> Centro Educativo Distrital Castilla (1999 – 2004)</li>
        </ul>
      </div>

      <div class="card">
        <h3>Educación Complementaria y Certificaciones</h3>
        <ul>
          <li><strong>Beca Latin American Talents & Diplomado en Data Analytics:</strong> (2020 – 2021)</li>
          <li><strong>Supervisión de proyectos de grado (Modalidad Capstone):</strong> Convenio Universidad del Rosario / UNOSEIS18 (2022 – Presente)</li>
          <li><strong>Fortalecimiento Empresarial:</strong> Cámara de Comercio de Bogotá (2013 – 2018)</li>
          <li><strong>Educación Continua en Matemáticas Financieras:</strong> (2017)</li>
        </ul>
      </div>

      <div class="card">
        <h3>Experiencia Profesional</h3>
        <p><strong>UNOSEIS18 (Start-up) — CFO & Business Development Manager</strong> (Dic 2012 – Presente)</p>
        <ul>
          <li>Supervisión del despliegue de planes de negocio estratégicos para cumplir objetivos contables, normativos y de ingresos.</li>
          <li>Análisis de información financiera detallada y preparación de reportes de rentabilidad.</li>
          <li>Diseño e implementación de estructuras de precios favorables y estrategias de marketing para nuevos clientes.</li>
          <li>Implementación de planes de acción correctiva para optimizar operaciones y mejorar eficiencia.</li>
        </ul>
      </div>

      <div class="card">
        <h3>Habilidades & Software</h3>
        <div class="skills-grid">
          <div class="skill-item"><strong>Power BI:</strong> 92%</div>
          <div class="skill-item"><strong>R Software:</strong> 75%</div>
          <div class="skill-item"><strong>Planeación Estratégica:</strong> 75%</div>
          <div class="skill-item"><strong>Diseño:</strong> 75%</div>
          <div class="skill-item"><strong>Gestión de Bases de Datos:</strong> 70%</div>
          <div class="skill-item"><strong>Python:</strong> 45%</div>
          <div class="skill-item"><strong>Sharp 3D:</strong> 45%</div>
          <div class="skill-item"><strong>MatLab:</strong> 25%</div>
        </div>
      </div>
    </section>

    <!-- PÁGINA 3: Proyectos -->
    <section id="proyectos" class="tab-content">
      <h2 class="section-title">Proyectos</h2>

      <div class="card">
        <h3>Análisis del Impacto de la Infraestructura Vial en el Desarrollo Regional de Colombia</h3>
        <p>
          Este proyecto analiza cómo las redes de transporte terrestre y la infraestructura vial afectan la conectividad, los costos de transporte y las brechas de productividad entre municipios y departamentos en Colombia.
        </p>
        <p>
          <strong>Resumen:</strong> Aprovechando metodologías de econometría espacial y análisis cuantitativo geográfico, la investigación aborda las disparidades regionales derivadas de las barreras geográficas y la red vial del país, evaluando el efecto de la accesibilidad y la aglomeración sobre las dinámicas de desarrollo territorial.
        </p>
      </div>
    </section>

  </main>

  <script>
    function switchTab(event, tabId) {
      const contents = document.querySelectorAll('.tab-content');
      contents.forEach(content => content.classList.remove('active'));

      const buttons = document.querySelectorAll('.tab-btn');
      buttons.forEach(btn => btn.classList.remove('active'));

      document.getElementById(tabId).classList.add('active');
      event.currentTarget.classList.add('active');
    }
  </script>
</body>
</html>