
import numpy as np
import time

troop_tier = 't10'
verbose = False
stats_t6 = [
    [243, 730],
    [730, 243],
    [974, 183]
]


stats_t10 = [
    [472, 1416],
    [1416, 472],
    [1888, 354]
]

stats_tg1 = [
    [491, 1473],
    [1473, 491],
    [1904, 388]
]
stats_tg2 = [
    [515, 1546],
    [1546, 515],
    [2062, 387]
]
stats_tg3 = [
    [541, 1624],
    [1624, 541],
    [2165, 406]
]


class Fighter:

    def __init__(self, init_dict):

        self.init_dict = init_dict
    
        self.load_dict()

        self.load_tier()

        self.current_troops = self.init_troops

    def load_dict(self):
        
        d = self.init_dict
        self.init_troops = d['init_troops']
        self.inf_attack = d['inf_attack']
        self.inf_defense = d['inf_defense']
        self.inf_lethality = d['inf_lethality']
        self.inf_health = d['inf_health']
        self.cav_attack = d['cav_attack']
        self.cav_defense = d['cav_defense']
        self.cav_lethality = d['cav_lethality']
        self.cav_health = d['cav_health']
        self.arc_attack = d['arc_attack']
        self.arc_defense = d['arc_defense']
        self.arc_lethality = d['arc_lethality']
        self.arc_health = d['arc_health']
        self.init_total_troops = np.sum(np.array(d['init_troops']))

        if "player_name" in d:
            self.player_name = d["player_name"]
        else:
            self.player_name = ''

        if "battle_name" in d:
            self.battle_name = d["battle_name"]
        else:
            self.battle_name = ''
        if "troop_tier" in d:
            self.troop_tier = d['troop_tier']
        else:
            self.troop_tier = 't10'

    def load_tier(self):

        if self.troop_tier == 't6':
            print('t6 troop!')
            self.units_stats = stats_t6

        if self.troop_tier == 't10':
            print('t10 troop!')
            self.units_stats = stats_t10

        if self.troop_tier == 'tg1':
            print('tg1 troop!')
            self.units_stats = stats_tg1

        if self.troop_tier == 'tg2':
            print('tg2 troop!')
            self.units_stats = stats_tg2

        if self.troop_tier == 'tg3':
            print('tg3 troop!')
            self.units_stats = stats_tg3


def get_dead(fighter, opponent, fighter_unittype, opponent_unittype):


    nfighter_0 = fighter.init_total_troops
    nopponent_0 = opponent.init_total_troops

    new_number = np.sqrt(np.min( [nfighter_0, nopponent_0])) # fighter.toto# 1 # 14.14 #nfighter / np.max([nfighter, nopponent ])

    units_statsf = fighter.units_stats
    units_statso = opponent.units_stats
    if fighter_unittype == 'inf':
        attack_factor = np.sqrt(fighter.current_troops[0]) * 10 * units_statsf[0][0] * (1 + fighter.inf_attack/100) *(1+fighter.inf_lethality/100) / 100 *new_number
    elif fighter_unittype == 'cav':
        attack_factor = np.sqrt(fighter.current_troops[1]) * 10 * units_statsf[1][0] * (1 + fighter.cav_attack/100) *(1+fighter.cav_lethality/100) / 100 *new_number
    elif fighter_unittype == 'arc':
        attack_factor = np.sqrt(fighter.current_troops[2]) * 10 * units_statsf[2][0] * (1 + fighter.arc_attack/100) *(1+fighter.arc_lethality/100) / 100 *new_number
   

    if opponent_unittype == 'inf':
        defense_factor = 10 * units_statso[0][1] * (1 + opponent.inf_defense/100) *(1+opponent.inf_health/100)# / 100
    elif opponent_unittype == 'cav':
        defense_factor = 10 * units_statso[1][1] * (1 + opponent.cav_defense/100) *(1+opponent.cav_health/100) #/ 100
    elif opponent_unittype == 'arc':
        defense_factor = 10 * units_statso[2][1] * (1 + opponent.arc_defense/100) *(1+opponent.arc_health/100)# / 100
   
    att_fac_bonus = 0
    def_fac_bonus = 0
    if (fighter_unittype == 'inf') and (opponent_unittype == 'cav'):
        #attack_factor *= 1.1
        att_fac_bonus += 0.1
    if (fighter_unittype == 'cav') and (opponent_unittype == 'inf'):
        #defense_factor *= 1.1
        def_fac_bonus += 0.1
    if (fighter_unittype == 'cav') and (opponent_unittype == 'arc'):
        #attack_factor *= 1.1
        att_fac_bonus += 0.1
    if (fighter_unittype == 'arc') and (opponent_unittype == 'inf'):
        #attack_factor *= 1.1
        att_fac_bonus += 0.1

    if fighter.troop_tier == 'tg3':
        if fighter_unittype == 'arc':
            att_fac_bonus += 0.5*((np.random.rand(1) > 0.8)[0])
        if fighter_unittype == 'cav':
            att_fac_bonus += 1*((np.random.rand(1) > 0.9)[0])
        if opponent_unittype == 'inf':
            def_fac_bonus = 0.36*((np.random.rand(1) > 0.75)[0])

    att_fac_bonus += 1
    def_fac_bonus += 1

    deads = attack_factor*att_fac_bonus/(defense_factor * def_fac_bonus)
    return deads


def round(fighter, opponent):

    fighter_current_troops = fighter.current_troops
    opponent_current_troops = opponent.current_troops

    if fighter_current_troops[0]> 0:
        if verbose:
            print('fighter has some infantry')
        if opponent_current_troops[0] - 0* opponent.dead_this_round[0]  > 0:
            if verbose:
                print('opponent has some infantry. inf1 vs inf2')
            dead = get_dead(fighter, opponent, 'inf', 'inf')
            opponent.dead_this_round[0] += dead

        elif opponent_current_troops[1] - 0*opponent.dead_this_round[1]  > 0:
            if verbose:
                print('opponent has no infantry, but some cavalry. inf1 vs cav2')
            dead = get_dead(fighter, opponent, 'inf', 'cav')
            opponent.dead_this_round[1] += dead

        else:
            if verbose:
                print('opponent has no cavalry, but some arcehry. inf1 vs arc2')
            dead = get_dead(fighter, opponent, 'inf', 'arc')
            opponent.dead_this_round[2] += dead
    else:
        if verbose:
            print('fighter has no infantry')

    if fighter_current_troops[1] > 0:
        if verbose:
            print('fighter has some cavalry')
        cav_ambush = (np.random.rand(1) > 0.8)[0]
        if cav_ambush:
            if verbose:
                print('cav do ambush!!')
            if opponent_current_troops[2] - 0*opponent.dead_this_round[2] > 0:
                if verbose:
                    print('opponent has arch, cav1 vs arc2')
                dead = get_dead(fighter, opponent, 'cav', 'arc')
                opponent.dead_this_round[2] += dead
                ## do the cav1 vs arc2
        else:
            if opponent_current_troops[0] - 0*opponent.dead_this_round[0]  > 0:
                if verbose:
                    print('opponent has some infantry. cav1 vs inf2')
                dead = get_dead(fighter, opponent, 'cav', 'inf')
                opponent.dead_this_round[0] += dead
            elif opponent_current_troops[1] - 0*opponent.dead_this_round[1] > 0:
                if verbose:
                    print('opponent has no infantry, but some cavalry. cav1 vs cav2')
                dead = get_dead(fighter, opponent, 'cav', 'cav')
                opponent.dead_this_round[1] += dead
            else:
                if verbose:
                    print('opponent has no cavalry, but some arcehry. cav1 vs arc2')
                dead = get_dead(fighter, opponent, 'cav', 'arc')
                opponent.dead_this_round[2] += dead
    else: 
        if verbose:
            print('fighter has no cav')

    if fighter_current_troops[2] > 0:
        if verbose:
            print('fighter has some archery')
        arc_volley = (np.random.rand(1) > 0.9)[0]
        if opponent_current_troops[0] - 0*opponent.dead_this_round[0] > 0:
            if verbose:
                print('opponent has some infantry. arc1 vs inf2')
            dead = get_dead(fighter, opponent, 'arc', 'inf')
            opponent.dead_this_round[0] += dead
        elif opponent_current_troops[1] - 0*opponent.dead_this_round[1] > 0:
            if verbose:
                print('opponent has no infantry, but some cavalry. arc1 vs cav2')
            dead = get_dead(fighter, opponent, 'arc', 'cav')
            opponent.dead_this_round[1] += dead
        else:
            if verbose:
                print('opponent has no cavalry, but some arcehry. arc1 vs arc2')
            dead = get_dead(fighter, opponent, 'arc', 'arc')
            opponent.dead_this_round[2] += dead
        if arc_volley:
            if verbose:
                print('Arch volley!')
            if opponent_current_troops[0] - 0*opponent.dead_this_round[0]  > 0:
                if verbose:
                    print('opponent has some infantry. arc1 vs inf2')
                dead = get_dead(fighter, opponent, 'arc', 'inf')
                opponent.dead_this_round[0] += dead
            elif opponent_current_troops[1] - 0*opponent.dead_this_round[1] > 0:
                if verbose:
                    print('opponent has no infantry, but some cavalry. arc1 vs cav2')
                dead = get_dead(fighter, opponent, 'arc', 'cav')
                opponent.dead_this_round[1] += dead
            else:
                if verbose:
                    print('opponent has no cavalry, but some arcehry. arc1 vs arc2')
                dead = get_dead(fighter, opponent, 'arc', 'arc')
                opponent.dead_this_round[1] += dead


def get_results(p_1, p_2):

    p_1.current_troops = p_1.init_troops.copy()
    p_2.current_troops = p_2.init_troops.copy()
    #print(p_1.current_troops)
    #print(p_2.current_troops)

    t0 = time.time()

    cont = True
    nb_round = 0
    while cont:
        nb_round += 1
        #if verbose:
        #    print('Round {}'.format(nb_round))

        p_1.dead_this_round = [0, 0, 0]
        p_2.dead_this_round = [0, 0, 0]
        round(p_1, p_2)
        round(p_2, p_1)

        ## update troops:
        p_1.current_troops[0] -= p_1.dead_this_round[0]
        p_1.current_troops[1] -= p_1.dead_this_round[1]
        p_1.current_troops[2] -= p_1.dead_this_round[2]

        p_2.current_troops[0] -= p_2.dead_this_round[0]
        p_2.current_troops[1] -= p_2.dead_this_round[1]
        p_2.current_troops[2] -= p_2.dead_this_round[2]
        #if verbose:
        #    print('-----------------------')
        #    print(p_1.current_troops, p_2.current_troops)
        #    print('-----------------------')
        if (np.clip(p_1.current_troops, 0, 10000000000).sum()<= 0) or (np.clip(p_2.current_troops, 0,10000000000).sum()<= 0):
            cont = False

    if verbose:
        print('-----------------------')
        print('End of battle')
        print('P1 has ', np.round(np.clip(p_1.current_troops, 0, 10000000000)))
        print('P2 has ', np.round(np.clip(p_2.current_troops, 0, 10000000000)))
        print('-----------------------')

    end_troops_p1 = np.round(np.clip(p_1.current_troops, 0, 10000000000))
    end_troops_p2 = np.round(np.clip(p_2.current_troops, 0, 10000000000))

    is_victory = end_troops_p1.sum() > end_troops_p2.sum()
    t1 = time.time()
    #print(t1-t0)
    return end_troops_p1, end_troops_p2, is_victory


def get_average_results(N, player1_, player2_):
    vic_tab = np.zeros(N) 
    for i in range(N):
        _, _, vic_tab[i] = get_results(player1_, player2_)

    return sum(vic_tab)/N


def compute_win_chances(player1_, player2_, n_battles, step=0.05, f_inf_min=0.40, f_inf_max=0.80, f_cav_min=0.0, f_cav_max=0.3):
    
    N_total = np.array(player1_.init_dict['init_troops']).sum()
    print(N_total)
    finf_tab = []
    fcav_tab = []
    farc_tab = []
    res_tab = []
    k = 0
    for f_inf in np.arange(f_inf_min, f_inf_max+.0001, step):
        for f_cav in np.arange(f_cav_min, np.min([1.00 - f_inf, f_cav_max+0.001]), step):
            f_arc = 1 - f_inf - f_cav
            N_inf = int(N_total * f_inf)
            N_cav = int(N_total * f_cav)
            N_arc = int(N_total * f_arc)

            player1_.init_troops = [N_inf, N_cav, N_arc]

            player1_.current_troops = player1_.init_troops.copy()
            player2_.current_troops = player2_.init_troops.copy()
            t0_1 = time.time()
            avg = get_average_results(n_battles, player1_, player2_)
            t0_2 = time.time()
            k += t0_2-t0_1

            finf_tab.append(f_inf)
            fcav_tab.append(f_cav)
            farc_tab.append(f_arc)
            res_tab.append(avg)

    t1 = time.time()

    print(k)
    return finf_tab, fcav_tab, farc_tab, res_tab
