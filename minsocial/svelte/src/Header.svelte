<script>
</script>

<main>
    <h1 class="Menu">@ Mentions</h1>
</main>

<style lang="scss">
    /*Colors*/
    $dark-gray: #252c2c;
    $medium-gray: #3c4444;
    $light-gray: #acacac;
    $white: white;
    $teal: #50c0cb;
    $dark-teal: #36676c;

    main {
        margin: 0;
        background-color: $dark-gray;
        color: $white;
        border-bottom: 3px solid $teal;
    }

    @media screen and (max-width:400px) {
        h1 {
            margin: 0;
            padding: 30px 20px 24px 20px;
            font-size: 18px;
            font-weight: 500;
        }
    }

    @media screen and (min-width:401px) {
        h1 {
            margin: 0;
            padding: 40px 20px 28px 20px;
            font-size: 32px;
            font-weight: 500;
        }
    }
</style>