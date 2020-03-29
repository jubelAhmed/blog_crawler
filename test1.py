# from bs4 import BeautifulSoup
#
# import os
#
# import os
# script_path = os.path.abspath(__file__) # i.e. /path/to/dir/foobar.py
# script_dir = os.path.split(script_path)[0] #i.e. /path/to/dir/
# rel_path = "index.html"
# abs_file_path = os.path.join(script_dir, rel_path)
#
# with open(abs_file_path) as fp:
#     soup = BeautifulSoup(fp,'html',multi_valued_attributes=None)
#
#
# soup = BeautifulSoup('<b class="boldest" id="1">Extremely bold</b>')
# tag = soup.b
# tag.name = 'p'
# print(type(tag))
# print(tag['class'])
#
# # print(soup.prittify())
# print(tag)
#
#

str= '1:00z0z_6e5Z1p9ULpY,1:00A0A_VtkhxqYgEg,1:00r0r_dOVNjl9YgJQ,1:00R0R_dwUvRfp7xE4,1:01313_cv1lFMWsUxZ,1:00s0s_vnQFAm9NvD,1:00A0A_9KjfKZuOCq7,1:01414_2ovsvaXrDXF,1:00j0j_acxFmwIM6wx,1:00I0I_krLRFgD0e4B,1:00x0x_jXRLErRMZIm,1:00a0a_dhIj29jkrEk,1:00I0I_6Q0C4AQLgbh,1:01313_6dZxnAORwm,1:00o0o_iOTPTii4IOw,1:00z0z_gLo5lDB3ik,1:00L0L_8KOoYinTYqS,1:00W0W_81qYYzwDM0R,1:00O0O_fXzIRQrYyoi,1:00z0z_iFG7F5Qtlk1,1:01212_5FpEPccfDXO,1:00p0p_4KP91aNYpVX,1:00Q0Q_hKQd2i0Ox21'

print(str.split(',')[0])