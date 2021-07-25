import pandas as pd

exoplanetas = pd.read_csv("Datos_exoplanetas.csv", index_col="Unnamed: 0")

# Get rid of every planet whose existence is disputed
exoplanetas = exoplanetas[exoplanetas["pl_controv_flag"] == 0]
# Drop the controversial column since it is not needed anymore
exoplanetas.drop(axis=1, labels='pl_controv_flag', inplace=True)

# Group planets by their names and put them together in the same row to remove all duplicates
df = exoplanetas.groupby(['pl_name']).agg({'ast_flag': 'first',
                                           'cb_flag': 'max',
                                           'disc_locale': 'first',
                                           'discoverymethod': 'first',
                                           'sy_snum': 'max',
                                           'dkin_flag': 'max',
                                           'etv_flag': 'max',
                                           'ima_flag': 'max',
                                           'obm_flag': 'max',
                                           'pl_masse': 'mean',
                                           'pl_massj': 'mean',
                                           'pl_msinie': 'mean',
                                           'pl_msinij': 'mean',
                                           'pl_orbeccen': 'max',
                                           'pl_orbper': 'max',
                                           'pl_orbsmax': 'max',
                                           'pl_rade': 'mean',
                                           'pl_radj': 'mean',
                                           'pl_tranmid': 'mean',
                                           'ptv_flag': 'max',
                                           'pul_flag': 'max',
                                           'rv_flag': 'max',
                                           'st_age': 'mean',
                                           'st_mass': 'mean',
                                           'st_rad': 'mean',
                                           'st_teff': 'mean',
                                           'sy_dist': 'mean',
                                           'sy_pnum': 'max',
                                           'sy_snum': 'max',
                                           'tran_flag': 'max'
                                           }).reset_index()

planets_discovered_PT = exoplanetas[exoplanetas['tran_flag'] == 1]  # Transit methods
planets_discovered_RV = exoplanetas[exoplanetas['rv_flag'] == 1]  # Radial velocity
planets_discovered_pulsar = exoplanetas[exoplanetas['pul_flag'] == 1]  # Pulsar Timing variations
planets_discovered_ptv = exoplanetas[exoplanetas['ptv_flag'] == 1]  # Pulsation timing variations
planets_discovered_ast = exoplanetas[exoplanetas['ast_flag'] == 1]  # Astrometric variations
planets_discovered_obm = exoplanetas[exoplanetas['obm_flag'] == 1]  # Orbital Brightness modulations
planets_discovered_micro = exoplanetas[exoplanetas['micro_flag'] == 1]  # Microlensing
planets_discovered_etv = exoplanetas[exoplanetas['etv_flag'] == 1]  # Eclipse Timing variations
planets_discovered_ima = exoplanetas[exoplanetas['ima_flag'] == 1]  # Direct imaging
planets_discovered_dkin = exoplanetas[exoplanetas['dkin_flag'] == 1]  # Disk kinematics
