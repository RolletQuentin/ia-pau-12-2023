<template>
    <div id="register">
        <slot></slot>
    </div>
</template>

<style lang="scss">
#register {
    border: 5px solid black;
    padding: 30px;

    form div {
        display: flex;
        flex-direction: column;

        label {
            margin-bottom: 3px;
        }

        input,
        textarea {
            margin-bottom: 20px;
            width: 200px;
            background-color: #eee;
            border: none;
            padding: 7px 3px;
        }
    }
}
</style>
