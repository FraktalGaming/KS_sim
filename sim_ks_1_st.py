import streamlit as st


import numpy as np
import time

import matplotlib.pyplot as plt
import sim_ks_lib as sksl

st.set_page_config(
    page_title="Frakinator",
    page_icon=":duck:",
    menu_items={
        'Report a bug': " mailto:fraktal0gaming@gmail.com",
    }
)

st.title('Frakinator -- WORK IN PROGRESS')

st.write('Made by [544] Frak. You can find me on the KS discord as Frak or frak._ , or you can send me an email fraktal0gaming at gmail com')

st.write("Stuck in mystic trials? Not sure what troop composition to use?\n \
    The Frakinator is here to help!"
    )

st.write("""
    The Frakinator accurately simulates the Kingshot battle mechanics,
    and is able to predict the outcome of a battle given the stats of the two opponents.
    The Frakinator is specifically designed to help you in the four trials that don't use heroes
    \n 
    It samples the various troop compositions, simulates a given number of battles and return the proportion of victories as a chance of victory.
""")




tab1, tab2, tab3 = st.tabs(["Mystic Trials", "Bear", "Acknowledgements"])

with tab1:




    st.markdown('### Instructions')
    st.write("""
        1. Enter your stats and the stats of the opponent, as they appear on a mystic trial battle report,\n 

        2. Vary the simulation parameters for more accurate results:\n 
            - number of battles: represents the number of battles that are simulated for each troop composition \n 
            - sparsity: number of troop composition that are sampled. Start with 0.05, and if finer sampling is required, use 0.025.\n 
            - Min infantry fraction: saves time by avoiding bad composition with low infantry
        3. For trials with heroes (Coliseum, Radiant Spire), since the tools does not (yet) include heroes, you can try to get a composition by decreasing the number of the enemy troops, while respecting the proportions. This is not as accurate as the other trials, but it can give an indication of the troop composition you can use.  
    """)


    with st.form('form1'):
        st.subheader('Your stats')

        col1, col2, col3 = st.columns(3)
        with col1:
            st.text('Infantry')
            inf_troops_p1 = st.number_input(
                'Initial infantry troops',
                min_value=0,
                value=50000,
                step=1,
                format="%d", key='inf_troops_p1')

            inf_att_p1 = st.number_input(
                'Infantry attack (in %)',
                min_value=0.0,
                value=200.0,
                step=1.0,
                format="%0.2f", key='inf_att_p1')

            inf_def_p1 = st.number_input(
                'Infantry defense (in %)',
                min_value=0.0,
                value=200.0,
                step=1.0,
                format="%0.2f", key='inf_def_p1')

            inf_let_p1 = st.number_input(
                'Infantry lethality (in %)',
                min_value=0.0,
                value=200.0,
                step=1.0,
                format="%0.2f", key='inf_let_p1')

            inf_hea_p1 = st.number_input(
                'Infantry health (in %)',
                min_value=0.0,
                value=200.0,
                step=1.0,
                format="%0.2f", key='inf_hea_p1')


        with col2:
            st.text('Cavalry')
            cav_troops_p1 = st.number_input(
                'Initial cavalry troops',
                min_value=0,
                value=50000,
                step=1,
                format="%d", key='cav_troops_p1')

            cav_att_p1 = st.number_input(
                'Cavalry attack (in %)',
                min_value=0.0,
                value=200.0,
                step=1.0,
                format="%0.2f", key='cav_att_p1')

            cav_def_p1 = st.number_input(
                'Cavalry defense (in %)',
                min_value=0.0,
                value=200.0,
                step=1.0,
                format="%0.2f", key='cav_def_p1')

            cav_let_p1 = st.number_input(
                'Cavalry lethality (in %)',
                min_value=0.0,
                value=200.0,
                step=1.0,
                format="%0.2f", key='cav_let_p1')

            cav_hea_p1 = st.number_input(
                'Cavalry health (in %)',
                min_value=0.0,
                value=200.0,
                step=1.0,
                format="%0.2f", key='cav_hea_p1')

        with col3: 
            st.text('Archery')
            arc_troops_p1 = st.number_input(
                'Initial archery troops',
                min_value=0,
                value=50000,
                step=1,
                format="%d", key='arc_troops_p1')

            arc_att_p1 = st.number_input(
                'Archery attack (in %)',
                min_value=0.0,
                value=200.0,
                step=1.0,
                format="%0.2f", key='arc_att_p1')

            arc_def_p1 = st.number_input(
                'Archery defense (in %)',
                min_value=0.0,
                value=200.0,
                step=1.0,
                format="%0.2f", key='arc_def_p1')

            arc_let_p1 = st.number_input(
                'Archery lethality (in %)',
                min_value=0.0,
                value=200.0,
                step=1.0,
                format="%0.2f", key='arc_let_p1')

            arc_hea_p1 = st.number_input(
                'Archery health (in %)',
                min_value=0.0,
                value=200.0,
                step=1.0,
                format="%0.2f", key='arc_hea_p1')

        st.subheader('Opponent stats')
        col4, col5, col6 = st.columns(3)
        with col4:
            st.text('Infantry')
            inf_troops_p2 = st.number_input(
                'Initial infantry troops',
                min_value=0,
                value=60000,
                step=1,
                format="%d", key='inf_troops_p2')

            inf_att_p2 = st.number_input(
                'Infantry attack (in %)',
                min_value=0.0,
                value=200.0,
                step=1.0,
                format="%0.2f", key='inf_att_p2')

            inf_def_p2 = st.number_input(
                'Infantry defense (in %)',
                min_value=0.0,
                value=200.0,
                step=1.0,
                format="%0.2f", key='inf_def_p2')

            inf_let_p2 = st.number_input(
                'Infantry lethality (in %)',
                min_value=0.0,
                value=200.0,
                step=1.0,
                format="%0.2f", key='inf_let_p2')

            inf_hea_p2 = st.number_input(
                'Infantry health (in %)',
                min_value=0.0,
                value=200.0,
                step=1.0,
                format="%0.2f", key='inf_hea_p2')


        with col5:
            st.text('Cavalry')
            cav_troops_p2 = st.number_input(
                'Initial cavalry troops',
                min_value=0,
                value=45000,
                step=1,
                format="%d", key='cav_troops_p2')

            cav_att_p2 = st.number_input(
                'Cavalry attack (in %)',
                min_value=0.0,
                value=200.0,
                step=1.0,
                format="%0.2f", key='cav_att_p2')

            cav_def_p2 = st.number_input(
                'Cavalry defense (in %)',
                min_value=0.0,
                value=200.0,
                step=1.0,
                format="%0.2f", key='cav_def_p2')

            cav_let_p2 = st.number_input(
                'Cavalry lethality (in %)',
                min_value=0.0,
                value=200.0,
                step=1.0,
                format="%0.2f", key='cav_let_p2')

            cav_hea_p2 = st.number_input(
                'Cavalry health (in %)',
                min_value=0.0,
                value=200.0,
                step=1.0,
                format="%0.2f", key='cav_hea_p2')

        with col6: 
            st.text('Archery')
            arc_troops_p2 = st.number_input(
                'Initial archery troops',
                min_value=0,
                value=45000,
                step=1,
                format="%d", key='arc_troops_p2')

            arc_att_p2 = st.number_input(
                'Archery attack (in %)',
                min_value=0.0,
                value=200.0,
                step=1.0,
                format="%0.2f", key='arc_att_p2')

            arc_def_p2 = st.number_input(
                'Archery defense (in %)',
                min_value=0.0,
                value=200.0,
                step=1.0,
                format="%0.2f", key='arc_def_p2')

            arc_let_p2 = st.number_input(
                'Archery lethality (in %)',
                min_value=0.0,
                value=200.0,
                step=1.0,
                format="%0.2f", key='arc_let_p2')

            arc_hea_p2 = st.number_input(
                'Archery health (in %)',
                min_value=0.0,
                value=200.0,
                step=1.0,
                format="%0.2f", key='arc_hea_p2')

        st.subheader('Simulation parameters')

        col7, col8 = st.columns(2)
        with col7:
            nbattles = st.number_input(
                'Number of battles simulated',
                min_value=10,
                max_value=100,
                value=10,
                step=10,
                format="%d", key='nbattles')
        with col8:
            stepp = st.number_input(
                'Sparsity',
                min_value=0.025,
                max_value=0.25,
                value=.05,
                step=0.025,
                format="%0.3f", key='step')
        col9, col10 = st.columns(2)    
        with col9:
            finfmin = st.number_input(
                'Min infantry fraction',
                min_value=0.,
                max_value=1.,
                value=.4,
                step=0.01,
                format="%0.2f", key='finfmin')
        with col10:
            finfmax = st.number_input(
                'Max infantry fraction',
                min_value=0.,
                max_value=1.,
                value=.8,
                step=0.01,
                format="%0.2f", key='finfmax')

        col11, col12 = st.columns(2)    
        with col11:
            fcavmin = st.number_input(
                'Min cavalry fraction',
                min_value=0.,
                max_value=1.,
                value=.15,
                step=0.01,
                format="%0.2f", key='fcavmin')
        with col12:
            fcavmax = st.number_input(
                'Max cavalry fraction',
                min_value=0.,
                max_value=1.,
                value=.3,
                step=0.01,
                format="%0.2f", key='fcavmax')


        submitted = st.form_submit_button("Create plots!")

    st.write('Modify the values above, and click the button!')



    p1_stats = {
        "init_troops": [inf_troops_p1, cav_troops_p1, arc_troops_p1],
        "inf_attack": inf_att_p1,
        "inf_defense": inf_def_p1,
        "inf_lethality": inf_let_p1,
        "inf_health": inf_hea_p1,
        "cav_attack": cav_att_p1,
        "cav_defense": cav_def_p1,
        "cav_lethality": cav_let_p1,
        "cav_health": cav_hea_p1,
        "arc_attack": arc_att_p1,
        "arc_defense": arc_def_p1,
        "arc_lethality": arc_let_p1,
        "arc_health": arc_hea_p1,
        "player_name": "Your name",
        "battle_name": ""
    }

    p2_stats = {
        "init_troops": [inf_troops_p2, cav_troops_p2, arc_troops_p2],
        "inf_attack": inf_att_p2,
        "inf_defense": inf_def_p2,
        "inf_lethality": inf_let_p2,
        "inf_health": inf_hea_p2,
        "cav_attack": cav_att_p2,
        "cav_defense": cav_def_p2,
        "cav_lethality": cav_let_p2,
        "cav_health": cav_hea_p2,
        "arc_attack": arc_att_p2,
        "arc_defense": arc_def_p2,
        "arc_lethality": arc_let_p2,
        "arc_health": arc_hea_p2,
        "player_name": "Your name",
        "battle_name": ""
    }


    if submitted:

        player1 = sksl.Fighter(p1_stats)
        player2 = sksl.Fighter(p2_stats)


        n_battles = nbattles
        step = stepp
        f_inf_min = finfmin

        finf_tab, fcav_tab, farc_tab, res_tab = sksl.compute_win_chances(
            player1, player2,
            n_battles, step,
            f_inf_min=f_inf_min, f_inf_max=finfmax,
            f_cav_min=fcavmin, f_cav_max=fcavmax
        )
        


        id_best = np.where(np.array(res_tab) == np.array(res_tab).max())[0][0]
        print(finf_tab[id_best])
        print(fcav_tab[id_best])
        print(farc_tab[id_best])
        finf_best = np.round(finf_tab[id_best], 2)
        fcav_best = np.round(fcav_tab[id_best], 2)
        farc_best = np.round(farc_tab[id_best], 2)

        min_val = np.array(res_tab).max()
        if min_val < 20:
            vmin = 20
        else:
            vmin = 100


        fig1 = plt.figure(2)
        ax = fig1.gca()

        sc = ax.scatter(finf_tab, fcav_tab, c=np.array(res_tab)*100, vmin=0)
        ax.plot(.50, .25, c='r', lw=0, marker='x', ms=5, label='50/25/25', mew=3)
        ax.plot(finf_best, fcav_best,  c='m', lw=0, marker='x', ms=3, label='Best {}/{}/{}'.format(int(finf_best*100), int(fcav_best*100), int(farc_best*100)), mew=3)
        ax.set_xlabel('infantry fraction')
        ax.set_ylabel('cavalry fraction')
        ax.set_xlim(-0.05, 1.05)
        ax.set_ylim(-0.05, 1.05)
        ax.legend()
        #ax.set_title(', {}'.format(player1.player_name, player1.battle_name)) 
        fig1.colorbar(sc, label='chances of victory [%] ')
        fig1.text(0.7, -0.15, 'Plot made with the Frakinator', size='small', transform=ax.transAxes)

        # fig2 = plt.figure(3)
        # plt.clf()
        # plt.scatter(farc_tab, finf_tab, c=np.array(res_tab)*100, vmin=0)
        # plt.plot(.25, .50, c='r', lw=0, marker='x', ms=5, label='50/25/25', mew=3)
        # plt.plot(farc_best, finf_best,  c='m', lw=0, marker='x', ms=3, label='Best {}/{}/{}'.format(int(finf_best*100), int(fcav_best*100), int(farc_best*100)), mew=3)
        # plt.xlabel('f_arc')
        # plt.ylabel('f_inf')
        # plt.xlim(-0.05, 1.05)
        # plt.ylim(-0.05, 1.05)
        # plt.legend()
        # plt.title('arc - inf ratio for {}, {}'.format(player1.player_name, player1.battle_name)) 
        # plt.colorbar(label='chances of victory [%] ')
        # plt.title('arc - inf ratio for {}, {}'.format(player1.player_name, player1.battle_name))



        st.pyplot(fig1)
        st.write("""
        You have an appromative {}\% chance to win with the following composition {}/{}/{}.
    """.format(int(min_val*100), int(100*finf_best), int(100*fcav_best), int(100*farc_best)))
        st.write("""
        The red cross indicate the classical 50/25/25 composition. 
        """)

    # st.pyplot(fig2)

            # fig = plt.figure(1, figsize=[fs/1.2 for fs in matplotlib.rcParams['figure.figsize']])
            # ax = fig.gca()
            # ax.errorbar(XX[:, 1], YY, yerr=sigma, fmt='k.', label='Training data')
            # ax.plot(x_2[:,1], x_2 @ w_ols, 'r-', label='OLS')
            # ax.plot(x_, alpha*x_ + b, 'b-', label='model')
            # ax.set_xlim(x_min, x_max)
            # ax.set_ylim(alpha *x_min + b-2*sigma, alpha *x_max + b + 2*sigma)
            # ax.set_xlabel('x', fontsize=14)
            # ax.set_ylabel('y', fontsize=14)
            # ax.legend()
            # st.pyplot(fig)



with tab2:
    with st.container():
        st.markdown('## Bear')
        st.write("""
        Total bear damage is the sum of the damage done independantly by infantry, cavalary and archery.
        The damage of each troop is:
        - proportional linearly to the attack of the rally leader
        - proportional linearly to the lethality of the rally leader
        - proportional to square root of the number of troops of a given type (Inf, Cav, or Arc)
         
        I'll explain the maths behind soon, but here is a small interactive model where you can modify the attack and lethality bonuses of the rally leader, and see how the damage would scale for 0, 10%, 20% and 30% infantry, as a function of the fraction of archers.\n 
        Note: The numbers given below are not the final bear damage, of course. This is just an illustration of how damage would varry if you change your troop composition, given the attack and lethality stats of your rally leader. Also, no hero are considered here. 
        """)

        col50, col51, col52 = st.columns(3)
        
        with col50:
            st.text('Infantry')
        
            inf_att_bear = st.number_input(
                'Infantry attack (in %)',
                min_value=0.0,
                value=400.0,
                step=25.0,
                format="%0.2f", key='inf_att_bear')
            
            inf_let_bear = st.number_input(
                'Infantry lethality (in %)',
                min_value=0.0,
                value=400.0,
                step=25.0,
                format="%0.2f", key='inf_let_bear')
        
        with col51:
            st.text('Cavalry')
        
            cav_att_bear = st.number_input(
                'Cavalry attack (in %)',
                min_value=0.0,
                value=400.0,
                step=25.0,
                format="%0.2f", key='cav_att_bear')
            
            cav_let_bear = st.number_input(
                'Cavalry lethality (in %)',
                min_value=0.0,
                value=400.0,
                step=25.0,
                format="%0.2f", key='cav_let_bear')


        with col52:
            st.text('Archery')
        
            arc_att_bear = st.number_input(
                'Archery attack (in %)',
                min_value=0.0,
                value=400.0,
                step=25.0,
                format="%0.2f", key='arc_att_bear')
            
            arc_let_bear = st.number_input(
                'Archery lethality (in %)',
                min_value=0.0,
                value=400.0,
                step=25.0,
                format="%0.2f", key='arc_let_bear')

    fa = np.arange(101)/100

    inf_att = inf_att_bear
    inf_let = inf_let_bear

    cav_att = cav_att_bear
    cav_let = cav_let_bear

    arc_att = arc_att_bear
    arc_let = arc_let_bear
 
    fig2 = plt.figure(3)
    ax2 = fig2.gca()


    a = (1+cav_att/100) * (1+cav_let/100)
    b = 4/3 * (1+arc_att/100) * (1+arc_let/100)*1.1
    c = 1/3 * (1+inf_att/100) * (1+inf_let/100)

    f_inf = 0
    f_arc = fa * (1-f_inf)
    res1 = (np.sqrt(1-f_arc-f_inf)* a + np.sqrt(f_arc) * b +  np.sqrt(f_inf) *c )
    ax2.plot(f_arc, res1, label=r"""$f_{\rm{inf}} = 0$""")

    f_inf = .1
    f_arc = fa * (1-f_inf)
    res1 = (np.sqrt(1-f_arc-f_inf)* a + np.sqrt(f_arc) * b+  np.sqrt(f_inf) *c)
    ax2.plot(f_arc, res1, label=r"""$f_{\rm{inf}} = 0.1$""")

    f_inf = .2
    f_arc = fa * (1-f_inf)
    res1 = (np.sqrt(1-f_arc-f_inf)* a + np.sqrt(f_arc) * b+  np.sqrt(f_inf) *c)
    ax2.plot(f_arc, res1, label=r"""$f_{\rm{inf}} = 0.2$""")

    f_inf = .3
    f_arc = fa * (1-f_inf)
    res1 = (np.sqrt(1-f_arc-f_inf)* a + np.sqrt(f_arc) * b+  np.sqrt(f_inf) *c)
    ax2.plot(f_arc, res1, label=r"""$f_{\rm{inf}} = 0.3$""")

    ax2.set_xlabel('f_arc')
    ax2.set_ylabel('Unscaled Total damage')
    fopt = b**2/(a**2+b**2)
    ax2.legend()

    ax2.axvline(fopt)

    fig2.text(0.7, -0.15, 'Plot made with the Frakinator', size='small', transform=ax2.transAxes)
    st.pyplot(fig2)




with tab3:
    with st.container():
        st.markdown('## Acknowledgements')
        st.write("""
        I used many sources to build this simulator.
        - https://kingshotsimulator.com : Obvisously.
        - https://sites.google.com/view/sos-guide-en : I think this is the source of all the WoS/KS material. Many, if not all, of the game mechanics are from this game (State of Survival).
        - https://github.com/request-laurent/sos.battle : The github of the SoS simulator.
        - Many, many thanks to my friends in #544 who helped me immensely for testing. 
        """)