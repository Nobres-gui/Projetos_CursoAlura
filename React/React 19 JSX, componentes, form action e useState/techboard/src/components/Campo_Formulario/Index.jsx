import './campo-formulario.estilos.css'
export function Campo_Formulario({ children }){
  return(
    <fieldset className="campo_form">
      {children}
    </fieldset>
  )
}