<script>
    import Header from "./Header.svelte";
    import Navbar_mobile from "./Navbar_mobile.svelte"
    import Navbar_desktop from "./Navbar_desktop.svelte"
    import NavbarMobile from "./Navbar_mobile.svelte";
</script>

<div class="desktop-format">
    <Navbar_desktop />
    <div class="content">
        <Header />
        <main>
            <ul>
                <li><a class="post" href="https://google.com">@user1 (Twitter) Hello World!</a></li>
                <li><a class="post" href="https://google.com">@user2 (Mastodon) Goodbye World!</a></li>
                <li><a class="post" href="https://google.com">@user1 (Twitter) Post!</a></li>
            </ul>
        </main>
    </div>    
</div>

<Navbar_mobile />


<style lang="scss">
    /*Colors*/
    $dark-gray: #252c2c;
    $medium-gray: #3c4444;
    $light-gray: #acacac;
    $white: white;
    $teal: #50c0cb;
    $dark-teal: #36676c;

    .desktop-format {
        height: 100vh;
    }
    main {
        margin: 0;
        width: 100%;
        background-color: $dark-gray;
    }

    .post {
        color: $white;
    }

    @media screen and (max-width:400px) {
        * {
            background-color: $dark-gray;
        }
        .desktop-format {  
            display: flex;
            flex-direction: column;
            align-items: stretch;
        }
        .content {
            height: 100%;
        }
        main {
            height: 100%;
        }
    }

    @media screen and (min-width:401px) {
        * {
            background-color: $dark-gray;
        }
        
        .desktop-format {
            display: flex;
            flex-direction: row;
        }
        .content {
            width: 100%;
        }
    }

</style>