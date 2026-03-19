import './campo-select.estilos.css'

export function Campo_Select(props){
  return(
        <select className="campo_select" id={props.id} name={props.name}>
            <option value="">Selecione uma opção</option>
            <option value="ia">IA</option>
            <option value="front_end">Front-End</option>
            <option value="back_end">Back-End</option>
            <option value="devops">Devops</option>
            <option value="data_science">Data Science</option>
            <option value="cloud">Cloud</option>
        </select>
    )
}