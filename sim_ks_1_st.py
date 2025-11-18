import streamlit as st


import numpy as np
import time

import matplotlib.pyplot as plt
import sim_ks_lib as sksl


st.sidebar.title("Stats")
with st.sidebar.form("toto"):  
    st.write('Yours stats')
    inf_troops_p1 = st.number_input(
        'Initial infantry troops',
        min_value=0,
        value=10000,
        step=None,
        format="%d", key='inf_troops_p1')
    cav_troops_p1 = st.number_input(
        'Initial cavalry troops',
        min_value=0,
        value=10000,
        step=None,
        format="%d", key='cav_troops_p1')
    arc_troops_p1 = st.number_input(
        'Initial archery troops',
        min_value=0,
        value=10000,
        step=None,
        format="%d", key='arc_troops_p1')

    inf_att_p1 = st.number_input(
        'Infantry attack (in %)',
        min_value=0.0,
        value=200.0,
        step=None,
        format="%0.2f", key='inf_att_p1')

    inf_def_p1 = st.number_input(
        'Infantry defense (in %)',
        min_value=0.0,
        value=200.0,
        step=None,
        format="%0.2f", key='inf_def_p1')

    inf_let_p1 = st.number_input(
        'Infantry lethality (in %)',
        min_value=0.0,
        value=200.0,
        step=None,
        format="%0.2f", key='inf_let_p1')

    inf_hea_p1 = st.number_input(
        'Infantry health (in %)',
        min_value=0.0,
        value=200.0,
        step=None,
        format="%0.2f", key='inf_hea_p1')
   
        
    cav_att_p1 = st.number_input(
        'Cavalry attack (in %)',
        min_value=0.0,
        value=200.0,
        step=None,
        format="%0.2f", key='cav_att_p1')

    cav_def_p1 = st.number_input(
        'Cavalry defense (in %)',
        min_value=0.0,
        value=200.0,
        step=None,
        format="%0.2f", key='cav_def_p1')

    cav_let_p1 = st.number_input(
        'Cavalry lethality (in %)',
        min_value=0.0,
        value=200.0,
        step=None,
        format="%0.2f", key='cav_let_p1')

    cav_hea_p1 = st.number_input(
        'Cavalry health (in %)',
        min_value=0.0,
        value=200.0,
        step=None,
        format="%0.2f", key='cav_hea_p1')
   
    arc_att_p1 = st.number_input(
        'Archery attack (in %)',
        min_value=0.0,
        value=200.0,
        step=None,
        format="%0.2f", key='arc_att_p1')

    arc_def_p1 = st.number_input(
        'Archery defense (in %)',
        min_value=0.0,
        value=200.0,
        step=None,
        format="%0.2f", key='arc_def_p1')

    arc_let_p1 = st.number_input(
        'Archery lethality (in %)',
        min_value=0.0,
        value=200.0,
        step=None,
        format="%0.2f", key='arc_let_p1')

    arc_hea_p1 = st.number_input(
        'Archery health (in %)',
        min_value=0.0,
        value=200.0,
        step=None,
        format="%0.2f", key='arc_hea_p1')
   

    st.write('Opponents stats')
    inf_troops_p2 = st.number_input(
        'Initial infantry troops',
        min_value=0,
        value=10000,
        step=None,
        format="%d")
    cav_troops_p2 = st.number_input(
        'Initial cavalry troops',
        min_value=0,
        value=10000,
        step=None,
        format="%d")
    arc_troops_p2 = st.number_input(
        'Initial archery troops',
        min_value=0,
        value=10000,
        step=None,
        format="%d")

    inf_att_p2 = st.number_input(
        'Infantry attack (in %)',
        min_value=0.0,
        value=200.0,
        step=None,
        format="%0.2f")

    inf_def_p2 = st.number_input(
        'Infantry defense (in %)',
        min_value=0.0,
        value=200.0,
        step=None,
        format="%0.2f")

    inf_let_p2 = st.number_input(
        'Infantry lethality (in %)',
        min_value=0.0,
        value=200.0,
        step=None,
        format="%0.2f")

    inf_hea_p2 = st.number_input(
        'Infantry health (in %)',
        min_value=0.0,
        value=200.0,
        step=None,
        format="%0.2f")
   
        
    cav_att_p2 = st.number_input(
        'Cavalry attack (in %)',
        min_value=0.0,
        value=200.0,
        step=None,
        format="%0.2f")

    cav_def_p2 = st.number_input(
        'Cavalry defense (in %)',
        min_value=0.0,
        value=200.0,
        step=None,
        format="%0.2f")

    cav_let_p2 = st.number_input(
        'Cavalry lethality (in %)',
        min_value=0.0,
        value=200.0,
        step=None,
        format="%0.2f")

    cav_hea_p2 = st.number_input(
        'Cavalry health (in %)',
        min_value=0.0,
        value=200.0,
        step=None,
        format="%0.2f")
   
    arc_att_p2 = st.number_input(
        'Archery attack (in %)',
        min_value=0.0,
        value=200.0,
        step=None,
        format="%0.2f")

    arc_def_p2 = st.number_input(
        'Archery defense (in %)',
        min_value=0.0,
        value=200.0,
        step=None,
        format="%0.2f")

    arc_let_p2 = st.number_input(
        'Archery lethality (in %)',
        min_value=0.0,
        value=200.0,
        step=None,
        format="%0.2f")

    arc_hea_p2 = st.number_input(
        'Archery health (in %)',
        min_value=0.0,
        value=200.0,
        step=None,
        format="%0.2f")
   

    submitted = st.form_submit_button("Create plots!")


st.write('Modify the values on the left, and click the button!')


#inf_att_p1 = st.number_input('Infantry attack (in %)', min_value=0.0, value=200.0, step=None, format="%0.2f", key=None, help=None, on_change=None, args=None, kwargs=None)
#def fc_titi():
#    st.write(inf_att_p1)


#button = st.button('titi', on_click=fc_titi)



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


    n_battles = 10
    step = 0.05
    f_inf_min = 0.1

    ta = time.time()
    finf_tab, fcav_tab, farc_tab, res_tab = sksl.compute_win_chances(player1, player2, n_battles, step, f_inf_min=f_inf_min)
    print(time.time()-ta)

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
    ax.set_xlabel('f_inf')
    ax.set_ylabel('f_cav')
    ax.set_xlim(-0.05, 1.05)
    ax.set_ylim(-0.05, 1.05)
    ax.legend()
    ax.set_title('inf - cav ratio for {}, {}'.format(player1.player_name, player1.battle_name)) 
    fig1.colorbar(sc, label='chances of victory [%] ')


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

