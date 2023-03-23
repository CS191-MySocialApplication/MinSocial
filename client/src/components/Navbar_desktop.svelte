<script>
</script>

<main>
    <nav class="nav-bar-desktop">
        <!--No icons yet. li placed in the meantime-->
        <ul>
            <li><a href="/home">Home</a></li>
            <li><a href="/messages">Messages</a></li>
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
        main {
            display: none;
        }
    }

    @media screen and (min-width:480px) and (max-width: 899px) {
        main {
            width: 24%;
            margin-right: 20px;
        }
    }

    @media screen and (min-width:900px) {
        main {
            width: 14%;
            margin-right: 20px;
        }
    }

</style>