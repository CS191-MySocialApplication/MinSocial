<script>
</script>

<main>
    <nav class="nav-bar-mobile">
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
    }

    @media screen and (max-width:400px) {
        .nav-bar-mobile {
            ul {
                display: flex;
                justify-content: space-around;
                align-items: center;
                padding: 0;
            }
            li {
                display: inline;
            }
        }
    }

    @media screen and (min-width:401px) {
        main {
            display: none;
        }
    }
</style>