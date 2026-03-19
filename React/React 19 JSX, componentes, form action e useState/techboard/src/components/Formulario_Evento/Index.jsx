import "./formulario-evento.estilos.css";
import { Campo_Formulario } from "../Campo_Formulario";
import { Campo_Label } from "../Campo_Label";
import { Campo_Input } from "../Campo_Input";
import { Titulo_Formulario } from "../Titulo_Formulario";
import { Campo_Select } from "../Campo_Select";
import { Formulario_Botao } from "../Formulario_Botao";

export function Formulario_Evento({ temas, adicionandoEventos }){

  function adicionarEvento(formData){
    console.log('Criando novo evento...', formData)
    const evento = {
      tema : temas.find((item) => { return item.id == formData.get('tema')}),
      capa : formData.get('txt_capa'),
      data : new Date(formData.get('campo_data')),
      titulo : formData.get('txt_titulo') 
    }
    adicionandoEventos(evento)
  }

  return(
    <form action={adicionarEvento} className="form_evento">
      <Titulo_Formulario titulo="Preencha para criar um evento:" />
      <div className="campos-form">
        <Campo_Formulario>
          <Campo_Label htmlFor="txt_titulo">
            Nome do evento:
          </Campo_Label>
          <Campo_Input type="text" id="txt_titulo" placeholder="Summer dev hits" />
        </Campo_Formulario>

          <Campo_Formulario>
          <Campo_Label htmlFor="txt_capa">
            Qual o endereço da imagem da capa:
          </Campo_Label>
          <Campo_Input type="text" name="txt_capa" id="txt_capa" placeholder="http://..." />
        </Campo_Formulario>

        <Campo_Formulario>
          <Campo_Label htmlFor="campo_data">
            Data do evento:
          </Campo_Label>
          <Campo_Input type="date" id="campo_data" name='campo_data' />
        </Campo_Formulario>


        <Campo_Formulario>
          <Campo_Label htmlFor="tema">
            Tema do evento:
          </Campo_Label>
          <Campo_Select itens={ temas } id='tema' name='tema'  />
        </Campo_Formulario>
      </div>

      <div className="form_acoes">
        <Formulario_Botao type="submit" texto="Criar Evento" />
      </div>
    </form>
  )

}