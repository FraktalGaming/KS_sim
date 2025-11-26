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




tab1, tab2, tab3, tab4 = st.tabs(["Mystic Trials", "Bear", "Theory-crafting","Acknowledgements"])

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
        col13, col14 = st.columns(2)
        with col13:            
            trial_name = st.selectbox(
                "Mystic trial",
                ("Forest of Life", "Crystal Cave", "Knowledge Nexus", "Molten Fort"),
            )
        with col14:
            player_name = st.text_input("Player name", "Enter your name here")

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
        print(player_name, trial_name, time.time())
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
        ax.set_title('{} - {}'.format(trial_name, player_name)) 
        fig1.colorbar(sc, label='chances of victory [%] ')
        fig1.text(0.7, -0.15, 'Plot made with the Frakinator', size='small', transform=ax.transAxes)

        st.pyplot(fig1)
        st.write("""
        You have an appromative {}\% chance to win with the following composition {}/{}/{}.
    """.format(int(min_val*100), int(100*finf_best), int(100*fcav_best), int(100*farc_best)))
        st.write("""
        The red cross indicates the classical 50/25/25 composition. 
        """)
        print('----------------------------------------')

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

    with st.form('form2'):
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
        submitted2 = st.form_submit_button("Create plots!")

    if submitted2:
        print('Bear tab was used')
        inf_att = inf_att_bear
        inf_let = inf_let_bear

        cav_att = cav_att_bear
        cav_let = cav_let_bear

        arc_att = arc_att_bear
        arc_let = arc_let_bear

        damage = []
        finf_tab2 = []
        fcav_tab2 = []
        farc_tab2 = []
        res_tab2 = []
        k = 0
        step = 0.025
        for f_inf in np.arange(0, 1.01, step):
            for f_cav in np.arange(0, np.min([1.00 - f_inf, 1.001]), step):
                f_arc = 1 - f_inf - f_cav

                a = (1+cav_att/100) * (1+cav_let/100)
                b = 4/3 * (1+arc_att/100) * (1+arc_let/100)*1.1
                c = 1/3 * (1+inf_att/100) * (1+inf_let/100)
                res1 = (np.sqrt(f_cav) * a + np.sqrt(f_arc) * b +  np.sqrt(f_inf) *c )

                finf_tab2.append(f_inf)
                fcav_tab2.append(f_cav)
                farc_tab2.append(f_arc)
                res_tab2.append(res1)

        id_best = np.where(np.array(res_tab2) == np.array(res_tab2).max())[0][0]
        max_dam = np.array(res_tab2).max()

        finf_best = np.round(finf_tab2[id_best], 2)
        fcav_best = np.round(fcav_tab2[id_best], 2)
        farc_best = np.round(farc_tab2[id_best], 2)

        fig2 = plt.figure(2)
        ax2 = fig2.gca()
        sc = ax2.scatter(finf_tab2, fcav_tab2, c=np.array(res_tab2)/max_dam, vmin=0.5)
        ax2.plot(.10, .10, c='r', lw=0, marker='x', ms=5, label='10/10/80', mew=3)
        ax2.plot(finf_best, fcav_best,  c='m', lw=0, marker='x', ms=3, label='Best {}/{}/{}'.format(int(finf_best*100), int(fcav_best*100), int(farc_best*100)), mew=3)
        ax2.set_xlabel('infantry fraction')
        ax2.set_ylabel('cavalry fraction')
        ax2.set_xlim(-0.05, 1.05)
        ax2.set_ylim(-0.05, 1.05)
        ax2.legend()
        #ax.set_title(', {}'.format(player1.player_name, player1.battle_name)) 
        fig2.colorbar(sc, label='Fraction of maximal damage')
        fig2.text(0.7, -0.15, 'Plot made with the Frakinator', size='small', transform=ax2.transAxes)
        st.pyplot(fig2)

        st.write("""
            With the leader stats you have entered, the best composition would be {}/{}/{}.
        """.format(int(100*finf_best), int(100*fcav_best), int(100*farc_best)))
        st.write("""
            The red cross indicates a typical 10/10/80 composition. 
            """)

with tab3: 
    st.markdown('## Theory-crafting')
    st.markdown("#### Disclaimer")
    st.write("""All the following is just a tentative to model the battle mechanics of the game. I have no knowledge of the real implementation done by the devs.
    All is based on previous investigations done by others, and by deductions and a lot of testing.
    Therefore I do not claim that any of the following is real nor accurate. That being said, I have done lots of tests, and I confidently believe that the bulk of what I am writing here is a good representation of the game mechanics. 
    There are still some elements that I don't know/understand yet.
    """)
    st.markdown("#### Notations")

    st.write(r"""
    We start by introducing some notations that will be useful. In all the calculation done in the battle mechanics attack and lethality always go together and are multiplied. 
    
    We thus introduce the "Attack Factor", noted $A$, as 
    $$
    A =  \left[1 + \frac{ \rm{attack\_bonus} }{100}\right] * \left[1 + \frac{ \rm{lethality\_bonus} }{100}\right].
    $$
    Similarly, we define the defense factor, noted $D$, as
    $$
    D =  \left[1 + \frac{ \rm{defense\_bonus} }{100}\right] * \left[1 + \frac{ \rm{health\_bonus} }{100}\right].
    $$

    In those two expressions, attack_bonus, lethality_bonus, defense_bonus, and health_bonus refer to the stats of a player that we can find in a typical battle report. This may look complicated, but this is just how you compute percentages.
    """)
    with st.container(border=True):
        st.write(r"""
            Example: if attack_bonus = +250% and lethality_bonus = +163%, the attack factor will be 
            $$
            A = (1+250/100) * (1+163/100) = 8.26.
            $$
        """)
    st.write(r"""
    Of course, each of the unit types (Infantry, Cavalry, Archer) will have their own attack and defense factors, that we will denote
    $A^{\rm{inf}}$ or $D^{\rm{arc}}$, depending on the unit type.
    """)

    st.markdown("#### The simplified kill formula")
    st.write(r"""
    At the core of every battle, is the kill formula that gives the number of killed/dead/removed units of one player due to the units of the other player.
    If we consider one player $p_1$ attacking a player $p_2$, the number of units of a given type of player $p_2$ killed by one type of units of player $p_1$ is given by:
    $$
    K_{{p_2}} \propto \sqrt{N_{{p_1}}}
    \frac{{(\rm{base\_att}*\rm{base\_let})_{p_1}}}{{(\rm{base\_def}*\rm{base\_hea})_{p_2}}}
    \frac{A_{\rm{p_1}}}{D_{\rm{p_2}}}
    $$

    Let's discuss this equation a bit.
    -  $\sqrt{N_{{p_1}}}$: here $N_{p_1}$ is the number of troop of a giben type (infantry, cavalry or archery). The fact that the number if kills depends on the square root of the number of troopd is very important.
    This term is increasing, if you add more more troops, you'll do more damage, but not in the proportion of the added troops. If you have twice the number of troops, the damage will not increase by a factor 2, but by a factor $\sqrt{2}\approx 1.4$. If you have 10 times  more troops, the damage is inxcreased by $\sqrt{10}\approx3.1$.

    - $ \frac{A_{\rm{p_1}}}{D_{\rm{p_2}}}$: This is the ratio of attack factor of the attacker's troop to the defense factor of the defender's troop. Thus attack and defence factor are always considered as a ratio.     
    
    - $\rm{base\_att}, \rm{base\_let}, \rm{base\_def}, \rm{base\_hea}$: This is where it gets interesting! Those numbers are the base stats of the troops that are considered in the battle. This makes sense: the stats bonuses that we see in battles reports are percentsge bonus. But percentage of what? 
    In the end, the stats bonues are applied to those base stats. But the exact values of those base are not given in the game. I strongly believe, and once again I can be wrong, that the values are the ones of a older game, called State of Survival. See the Acknowledgment tab for a link.
    Also, $\rm{base\_let}$ anbd $\rm{base\_def}$ are always the same for all the troop and all the tier, and this common value is 10. But those two number simplify in the kill formula and we are left with just two numbers for troop/tier:
        - $\rm{base\_att}$
        - $\rm{base\_hea}$

    You can find the values for the units on the SoS fan website. One interesting thing is that we seems to always have the following relations:
    - Attack_inf = Health_cav = 1/3 Health_inf = 1/3 Attack_cav
    - Attack_inf = 4/3 Health_arc = 1/4 Attack_arc
    """)

    st.write(r"""
    To be continued.
    """)

with tab4:
    with st.container():
        st.markdown('## Acknowledgements')
        st.write("""
        I used many sources to build this simulator.
        - https://kingshotsimulator.com : Obvisously.
        - https://sites.google.com/view/sos-guide-en : I think this is the source of all the WoS/KS material. Many, if not all, of the game mechanics are from this game (State of Survival).
        - https://github.com/request-laurent/sos.battle : The github of the SoS simulator.
        - Many, many thanks to my friends in #544 who helped me immensely for testing. 
        """)