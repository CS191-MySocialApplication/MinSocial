<script>
</script>

<main>
    <nav class="nav-bar-desktop">
        <!--No icons yet. li placed in the meantime-->
        <ul>
            <li><a href="login.html">DMs</a></li>
            <li><a href="login.html">Log out</a></li>
        </ul>
    </nav>
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
        background-color: $teal;
        color: $white;
        border-bottom: 3px solid $teal;
    }

    @media screen and (max-width:400px) {
        main {
            display: none;
        }
    }

    @media screen and (min-width:401px) {

        main {
            width: 16%;
        }
    }
</style>