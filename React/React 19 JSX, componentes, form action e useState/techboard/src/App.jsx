import "./App.css";
import { Formulario_Evento } from "./components/Formulario_Evento/Index";
import { Tema } from "./components/Tema";
import { Banner } from "./components/Banner";
import { Card_Eventos } from "./components/Card_Eventos";
import { useState } from "react";

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

  const [eventos, setEventos] = useState([
    {
      capa : 'http://raw.githubusercontent.com/viniciosneves/tecboard-assets/refs/heads/main/imagem_1.png',
      tema : tema[0],
      data : new Date(),
      titulo : 'Mulheres no Front' 
    }
  ])

  function salvarEventos( evento ){
    // eventos.push(evento);
    setEventos([...eventos, evento])
    console.log("Evento salvo", evento);
  }

  return (
    <main>
      <header className="header_main">
        <img src="/Logo.png" alt="image" />
      </header>
      <Banner/>
      <Formulario_Evento temas={tema} adicionandoEventos={salvarEventos}/>

      <section className="container_eventos">
        {/* É um for passando por todos os temas da const tema no app.jsx  */}
        {tema.map(function ( tema ){
          if(!eventos.some((evento) => {return evento.tema.id == tema.id})){
            return null
          }

            return  (
              <section key={tema.id}>
                <Tema tema={tema} />
                <div className="eventos">
                  {eventos.filter((evento) => {return evento.tema.id == tema.id})
                  .map((evento, index) => {
                    return <Card_Eventos evento={ evento } key={index}/>
                  })}
                </div>
              </section>
            )
          })
        }
      </section>

    </main>
  );
}

export default App;
