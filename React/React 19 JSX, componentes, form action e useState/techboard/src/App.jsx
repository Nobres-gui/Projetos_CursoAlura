import "./App.css";
import { Formulario_Evento } from "./components/Formulario_Evento/Index";


function App() {
  return (
    <main>
      <header className="header_main">
        <img src="/Logo.png" alt="image" />
      </header>
      <section className="section_banner">
        <img src="/banner.png" alt="Logo" className="section_banner-img" />
      </section>
      <Formulario_Evento/>
    </main>
  );
}

export default App;
