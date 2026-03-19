import './card-eventos.estilos.css'

export function Card_Eventos({ evento }) {
    return (
        <div className='card_evento'>
                <img src={evento.capa} alt={evento.titulo} />  
                <div className="card_corpo">
                    <p className="evento_tag">
                        {evento.tema.nome}
                    </p>
                    <p className='evento_data'>
                        {evento.data.toLocaleDateString('pt-BR')}
                    </p>
                    <h4 className='evento_tiutlo'>{evento.titulo}</h4>
                </div>    
        </div>
    )
}