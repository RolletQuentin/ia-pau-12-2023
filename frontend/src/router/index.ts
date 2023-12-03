import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import RecomandedProject from '@/views/RecomandedProject.vue'
import RegisterView from '../views/RegisterView.vue'
import ProjectView from '../views/ProjectView.vue'
import RecomandedUserByProject from '../views/RecommandedUserByProject.vue'
import RecommandedProjectByUser from '../views/RecommandedProjectByUser.vue'

const router = createRouter({
    history: createWebHistory(import.meta.env.BASE_URL),
    routes: [
        {
            path: '/',
            name: 'home',
            component: HomeView
        },
        {
            path: '/inscription',
            name: 'register',
            component: RegisterView
        },
        {
            path: '/projets',
            name: 'projects',
            component: ProjectView
        },
        {
            path: '/recommandation-projet',
            name: 'recommandation',
            component: RecomandedProject
        },
        {
            path: '/recommandation-utilisateur',
            name: 'userRecommandation',
            component: RecomandedUserByProject
        },
        {
            path: '/recommandation-projet-par-utilisateur',
            name: 'projectRecommandationByUser',
            component: RecommandedProjectByUser
        }
    ]
})

export default router
