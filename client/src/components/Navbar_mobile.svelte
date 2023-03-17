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

<style>
    main {
        margin: 0;
        background-color: #50c0cb;
        color: white;
    }

    @media screen and (max-width:479px) {
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

    @media screen and (min-width:480px) {
        main {
            display: none;
        }
    }
</style>