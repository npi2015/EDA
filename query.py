import pyvo as vo
import pandas as pd
tap_service = vo.dal.TAPService(" https://exoplanetarchive.ipac.caltech.edu/TAP")
tap_results = tap_service.search("""SELECT pl_name, pl_controv_flag, sy_snum, sy_pnum, cb_flag, discoverymethod, disc_locale, rv_flag, pul_flag, ptv_flag,
                                    tran_flag, ast_flag, obm_flag, micro_flag, etv_flag, ima_flag, dkin_flag, pl_orbper, pl_orbsmax, pl_rade, pl_radj, 
                                    pl_masse, pl_massj, pl_msinie, pl_msinij, pl_orbeccen, pl_tranmid, st_teff, st_rad, st_mass, st_age, sy_dist, rowupdate FROM PS""")
data = pd.DataFrame(tap_results)
data.to_csv("Datos_exoplanetas.csv")
print("Done")