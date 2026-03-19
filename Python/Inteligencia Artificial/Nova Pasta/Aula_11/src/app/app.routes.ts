import { Routes } from '@angular/router';

import { Home } from './componentes/home/home';
import { Pagina1 } from './componentes/pagina1/pagina1';
import { Pagina2 } from './componentes/pagina2/pagina2';
import { Sobre } from './componentes/sobre/sobre';
import { NotFound } from './componentes/not-found/not-found';


export const routes: Routes = [
    { path: '', component: Home },
    { path: 'pagina1', component: Pagina1 },
    { path: 'pagina2', component: Pagina2 },
    { path: 'sobre', component: Sobre },
    { path: '**', component: NotFound }
];
