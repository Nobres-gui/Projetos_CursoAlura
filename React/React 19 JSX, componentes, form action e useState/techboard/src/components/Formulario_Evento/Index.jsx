import "./formulario-evento.estilos.css";
import { Campo_Formulario } from "../Campo_Formulario";
import { Campo_Label } from "../Campo_Label";
import { Campo_Input } from "../Campo_Input";
import { Titulo_Formulario } from "../Titulo_Formulario";
import { Campo_Select } from "../Campo_Select";
import { Formulario_Botao } from "../Formulario_Botao";

export function Formulario_Evento(){
  return(
    <form action="" className="form_evento">
      <Titulo_Formulario titulo="Preencha para criar um evento:" />
      <div className="campos-form">
        <Campo_Formulario>
          <Campo_Label htmlFor="txt_nome">
            Nome do evento:
          </Campo_Label>
          <Campo_Input type="text" id="txt_nome" placeholder="Summer dev hits" />
        </Campo_Formulario>

      
        <Campo_Formulario>
          <Campo_Label htmlFor="txt_data">
            Data do evento:
          </Campo_Label>
          <Campo_Input type="date" id="txt_data" />
        </Campo_Formulario>


        <Campo_Formulario>
          <Campo_Label htmlFor="txt_tema">
            Tema do evento:
          </Campo_Label>
          <Campo_Select />
        </Campo_Formulario>
      </div>

      <div className="form_acoes">
        <Formulario_Botao type="submit" texto="Criar Evento" />
      </div>
    </form>
  )

}