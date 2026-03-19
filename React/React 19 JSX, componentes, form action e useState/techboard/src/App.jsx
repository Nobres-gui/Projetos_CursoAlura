import "./App.css";
import { Formulario_Evento } from "./components/Formulario_Evento/Index";
import { Tema } from "./components/Tema";
import { Banner } from "./components/Banner";

function App() {

  const tema = [
  {
    id:1,
    nome: 'front-end'
  },
  {
    id: 2,
    nome: 'back-end'
  },
  {
    id: 3,
    nome:'devops'
  },
  {
    id:4,
    nome: 'inteligência artificial'
  },
  {
    id:5,
    nome: 'data science'
  },
  {
    id:6,
    nome: 'cloud'
  }
  ]

  return (
    <main>
      <header className="header_main">
        <img src="/Logo.png" alt="image" />
      </header>
      <Banner/>
      <Formulario_Evento/>

      {/* É um for passando por todos os temas da const tema no app.jsx  */}
      {tema.map(function ( item ){
        return  (
          <section>
            <Tema tema={item} />
          </section>
        )
      })
      }

    </main>
  );
}

export default App;
