<template>
    <div class="spacer"></div>
    <header>
        <img :src="HBNLogo" />
        <nav>
            <div><a>Inscription</a></div>
            <div><a>Les projets</a></div>
            <div><a>Les associations</a></div>
        </nav>
    </header>
</template>

<script lang="ts">
import HBNLogo from '@/assets/images/logo_hbn.png'

export default {
    setup() {
        return {
            HBNLogo
        }
    }
}
</script>

<style lang="scss">
.spacer {
    /* same as height of the header */
    height: 180px;
}
header {
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

            a {
                text-transform: uppercase;
                font-weight: 600;
            }
        }
    }
}
</style>
