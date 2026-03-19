import './campo-select.estilos.css'

export function Campo_Select({ itens, ...rest }){
  return(
        <select {...rest} className="campo_select" defaultValue=''>
            <option value="" disabled>Selecione uma opção</option>
            {console.log("Itens na lista: " + itens)}
            {
            itens.map(( item ) => {
                    return  <option key={item.id} value={item.id}>{item.nome}</option>
                    
            })
            }

        </select>
    )
}