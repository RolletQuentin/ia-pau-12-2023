<template>
    <div class="spacer"></div>
    <header>
        <img :src="HBNLogo" />
        <nav>
            <div>
                <router-link class="link" :to="{ name: 'register' }">Inscription</router-link>
            </div>
            <div><router-link class="link" :to="{ name: 'home' }">Les projets</router-link></div>
            <div>
                <router-link class="link" :to="{ name: 'home' }">Les associations</router-link>
            </div>
        </nav>
    </header>
</template>

<script lang="ts">
import HBNLogo from '@/assets/images/logo_hbn.png'
import { RouterLink } from 'vue-router'

export default {
    components: {
        RouterLink
    },
    setup() {
        return {
            HBNLogo
        }
    }
}
</script>

<style lang="scss" scoped>
.spacer {
    /* same as height of the header */
    height: 180px;
}
header {
    background-color: white;
    box-shadow: 0 0 10px 0 rgba(0, 0, 0, 0.3);
    position: fixed;
    width: 100%;
    height: 100px;

    img {
        position: absolute;
        width: 150px;
        top: 30px;
        left: 200px;
        transition: all 0.5 ease;
    }

    nav {
        position: absolute;
        top: 40px;
        left: 400px;
        display: flex;

        div {
            margin-left: 15px;

            .link {
                color: inherit;
                text-decoration: none;
                text-transform: uppercase;
                font-weight: 600;
            }
        }
    }
}
</style>
