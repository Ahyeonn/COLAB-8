import {createRouter, createWebHistory} from 'vue-router'
import store from '@/store/index'
import HomeView from '@/views/HomeView'
import DashboardView from "@/views/DashboardView";
import ContactInfo from "@/views/ContactInfo";
import LogIn from "@/views/auth/LogIn";
import SignUp from "@/views/auth/SignUp";
import NotFound from '@/views/NotFound.vue';
import MeetingRespond from "@/views/MeetingRespond";
import MeetingDetails from "@/views/MeetingDetails";


function authGuard(to, from, next) {
    if (!store.state.auth.isLoggedIn || store.state.auth.isLoggedIn === 'false') {
        next({name: 'LogIn'})
    } else {
        next()
    }
}

const routes = [
    {
        path: '/',
        name: 'home',
        component: HomeView
    },
    {
        path: '/rsvp/:id',
        name: 'MeetingRespond',
        component: MeetingRespond
    },
    {
        path: '/dashboard',
        name: 'dashboard',
        component: DashboardView,
        beforeEnter: authGuard
    },
    {
        path: '/events/:id',
        name: 'MeetingDetails',
        component: MeetingDetails
    },
    {
        path: '/how-it-works',
        name: 'HowItWorks',
        component: () => import('@/views/HowItWorks.vue')
    },
    {
        path: '/contact-info',
        name: 'ContactInfo',
        component: ContactInfo
    },
    {
        path: '/meeting-confirmation',
        name: 'MeetingConfirmation',
        component: () => import('@/views/MeetingConfirmation.vue')
    },
    {
        path: '/meeting-created',
        name: 'MeetingCreated',
        component: () => import('@/views/MeetingCreated.vue')
    },
    {
        path: '/log-in',
        name: 'LogIn',
        component: LogIn
    },
    {
        path: '/sign-up',
        name: 'SignUp',
        component: SignUp
    },
    {
        path: '/about',
        name: 'about',
        // route level code-splitting
        // this generates a separate chunk (about.[hash].js) for this route
        // which is lazy-loaded when the route is visited.
        component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
    },
    {
        path: '/:notFound(.*)',
        component: NotFound,
    },
]

const router = createRouter({
    history: createWebHistory(process.env.BASE_URL),
    routes
})

export default router
