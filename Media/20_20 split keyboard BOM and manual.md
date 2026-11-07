# 20 20 split keyboard

**Features:**

**Hotswap**  
**Wireless:** Bluetooth support via ZMK.  
**Customizable:**  via ZMK Studio, at [zmk.studio](https://zmk.studio/)

**Layout**: Plank-ish 40% when magnetically attached, ortholinear 24 + 24 when split

**Build Video:** [YouTube](https://www.youtube.com/watch?v=XWv2SwuP9wc)  
**Firmware and more details**: [GitHub](https://github.com/vostoklabs/zmk-config-ortho20_20)

# 

# 

Pinout

Left Half                                              Right Half

|Columns:  0 - 106 1 - 104 2 - 011 3 - 100 4 - 024 5 - 022|Rows:   0 - 113 1 - 111 2 - 010 3 - 009||Columns:   0 - 106 1 - 104 2 - 011 3 - 100 4 - 024 5 - 022|Rows:   0 - 113 1 - 111 2 - 010 3 - 009|
|-|-|-|-|-|

# 

# Bill of materials

Assuming you have solder, solder iron, and some [wires](https://www.aliexpress.com/item/1005005048098404.html?spm=a2g0o.order_list.order_list_main.73.47741802kB9uqg)  
Additionally you will need some [rubber feet](https://www.aliexpress.com/item/1005002705337380.html?spm=a2g0o.productlist.main.7.74e944c7ipPwm5&algo_pvid=7c058d91-6ec7-4761-8e4c-82b9db734807&algo_exp_id=7c058d91-6ec7-4761-8e4c-82b9db734807-6&pdp_ext_f=%257B%2522order%2522%253A%2522157%2522%252C%2522eval%2522%253A%25221%2522%252C%2522fromPage%2522%253A%2522search%2522%257D&pdp_npi=6%2540dis%2521EUR%25211.53%25211.54%2521%2521%252112.25%252112.25%2521%25402103985c17692778254916662e525b%252112000041888154188%2521sea%2521HR%25216267174471%2521X%25211%25210%2521n_tag%253A-29919%253Bd%253Ae5d82de9%253Bm03_new_user%253A-29895&curPageLogUid=h4db4KzhGvYu&utparam-url=scene%253Asearch%257Cquery_from%253A%257Cx_object_id%253A1005002705337380%257C_p_origin_prod%253A), heatshrinks, hot glue and superglue

|Item|Link|Amount|
|-|-|-|
|Mechanical Cherry switches|[Link](https://www.aliexpress.com/item/1005007345651159.html?spm=a2g0o.productlist.main.3.1c0c5261aCURnr&algo_pvid=b00fd779-7665-47e9-ae03-470b540f6337&algo_exp_id=b00fd779-7665-47e9-ae03-470b540f6337-2&pdp_ext_f=%257B%2522order%2522%253A%25226394%2522%252C%2522eval%2522%253A%25221%2522%252C%2522orig_sl_item_id%2522%253A%25221005007345651159%2522%252C%2522orig_item_id%2522%253A%25221005009261993092%2522%252C%2522fromPage%2522%253A%2522search%2522%257D&pdp_npi=6%2540dis%2521EUR%25215.95%25212.98%2521%2521%252148.40%252124.20%2521%2540210384cc17589018536814612e5c26%252112000040355282124%2521sea%2521HR%25216267174471%2521X%25211%25210%2521n_tag%253A-29919%253Bd%253Ae5d82de9%253Bm03_new_user%253A-29895&curPageLogUid=zCC6svikv5Hc&utparam-url=scene%253Asearch%257Cquery_from%253A%257Cx_object_id%253A1005007345651159%257C_p_origin_prod%253A1005009261993092)|48|
|Pro micro NRF52840 controller ( Nice!Nano v2 clone)|[Link](https://www.aliexpress.com/item/1005006995289476.html?spm=a2g0o.productlist.main.3.54714221NO3mPU&algo_pvid=018aecb1-eafc-46ed-bf24-799c5e0c8c98&algo_exp_id=018aecb1-eafc-46ed-bf24-799c5e0c8c98-6&pdp_ext_f=%257B%2522order%2522%253A%25221766%2522%252C%2522eval%2522%253A%25221%2522%252C%2522orig_sl_item_id%2522%253A%25221005006995289476%2522%252C%2522orig_item_id%2522%253A%25221005006599766097%2522%252C%2522fromPage%2522%253A%2522search%2522%257D&pdp_npi=6%2540dis%2521EUR%25216.30%25213.15%2521%2521%252151.30%252125.65%2521%25402103835c17589020591883661e413f%252112000038985691707%2521sea%2521HR%25216267174471%2521X%25211%25210%2521n_tag%253A-29919%253Bd%253Ae5d82de9%253Bm03_new_user%253A-29895&curPageLogUid=VJ4Cad4XkmFS&utparam-url=scene%253Asearch%257Cquery_from%253A%257Cx_object_id%253A1005006995289476%257C_p_origin_prod%253A1005006599766097)|2|
|Hot Swap Sockets  For Mx Cherry|[Link](https://www.aliexpress.com/item/1005004290562374.html?spm=a2g0o.productlist.main.26.12fd18511ljxkV&algo_pvid=96bda181-c932-42c1-a6f5-b45411ff5c89&algo_exp_id=96bda181-c932-42c1-a6f5-b45411ff5c89-25&pdp_ext_f=%257B%2522order%2522%253A%2522326%2522%252C%2522eval%2522%253A%25221%2522%252C%2522fromPage%2522%253A%2522search%2522%257D&pdp_npi=6%2540dis%2521EUR%25214.47%25214.17%2521%2521%25215.04%25214.70%2521%2540211b815c17742633658514359e7479%252112000028647038706%2521sea%2521HR%25216267174471%2521X%25211%25210%2521n_tag%253A-29919%253Bd%253Ae5d82de9%253Bm03_new_user%253A-29895&curPageLogUid=oQQIaalNlcGV&utparam-url=scene%253Asearch%257Cquery_from%253A%257Cx_object_id%253A1005004290562374%257C_p_origin_prod%253A)|48|
|Diodes 1N4148|[Link](https://www.aliexpress.com/item/1005006245109375.html?spm=a2g0o.productlist.main.7.5f80648d0kGwN4&algo_pvid=28c31425-6c38-46a6-8a23-bc7315cb9f00&algo_exp_id=28c31425-6c38-46a6-8a23-bc7315cb9f00-6&pdp_ext_f=%257B%2522order%2522%253A%2522973%2522%252C%2522eval%2522%253A%25221%2522%252C%2522fromPage%2522%253A%2522search%2522%257D&pdp_npi=6%2540dis%2521EUR%25211.75%25211.14%2521%2521%252114.21%25219.26%2521%25402103919917589021056008905e2bbe%252112000036448323916%2521sea%2521HR%25216267174471%2521X%25211%25210%2521n_tag%253A-29919%253Bd%253Ae5d82de9%253Bm03_new_user%253A-29895&curPageLogUid=OhJwy5f5LVsx&utparam-url=scene%253Asearch%257Cquery_from%253A%257Cx_object_id%253A1005006245109375%257C_p_origin_prod%253A)|48|
|M2, 10 mm Socket Head Cap Machine Screws (SHCS)|[Link](https://eu.store.bambulab.com/products/m2-socket-head-cap-machine-screws-shcs?id=48672759054684)|4|
|M2, 4 mm Socket Head Cap Machine Screws (SHCS)|[Link](https://eu.store.bambulab.com/products/m2-socket-head-cap-machine-screws-shcs?id=48672758923612)|4|
|M2, 6mm stand offs|[Link](https://www.aliexpress.com/item/1005006049595637.html?spm=a2g0o.store_pc_home.promoteWysiwyg_2002746201276.1005006049595637)|4|
|4 by 2 mm magnets|[Link](https://eu.store.bambulab.com/products/round-magnet?id=47966966579548)|6|
|Kapton tape|[Link](https://www.aliexpress.com/item/1005007518587827.html?spm=a2g0o.productlist.main.2.202f49e3GVOXp0&algo_pvid=b11967b5-32c6-4440-93a4-052201d52ac3&algo_exp_id=b11967b5-32c6-4440-93a4-052201d52ac3-4&pdp_ext_f=%257B%2522order%2522%253A%252216925%2522%252C%2522eval%2522%253A%25221%2522%252C%2522fromPage%2522%253A%2522search%2522%257D&pdp_npi=6%2540dis%2521EUR%25211.54%25211.54%2521%2521%252112.49%252112.49%2521%25402103891017590609061623435ece05%252112000041103956429%2521sea%2521HR%25216267174471%2521X%25211%25210%2521n_tag%253A-29919%253Bd%253Ae5d82de9%253Bm03_new_user%253A-29895&curPageLogUid=FLnTGx29WStB&utparam-url=scene%253Asearch%257Cquery_from%253A%257Cx_object_id%253A1005007518587827%257C_p_origin_prod%253A)|1|
|Copper wire|[Link](https://www.aliexpress.com/item/1005009078359338.html?spm=a2g0o.order_list.order_list_main.56.47741802kB9uqg)|1|
|801350 3.7V Li-Po Battery|[Link](https://www.aliexpress.com/item/1005007117105334.html?spm=a2g0o.productlist.main.4.3fcd29d0Flx8XT&algo_pvid=db92b8f4-930e-4a41-bd0d-699054b92b6c&algo_exp_id=db92b8f4-930e-4a41-bd0d-699054b92b6c-4&pdp_ext_f=%257B%2522order%2522%253A%2522114%2522%252C%2522eval%2522%253A%25221%2522%252C%2522fromPage%2522%253A%2522search%2522%257D&pdp_npi=6%2540dis%2521EUR%252116.89%25219.46%2521%2521%2521135.25%252175.74%2521%2540211b80f717644487606471968e4c08%252112000039455075334%2521sea%2521HR%25216267174471%2521X%25211%25210%2521n_tag%253A-29919%253Bd%253Ae5d82de9%253Bm03_new_user%253A-29895&curPageLogUid=DpbnRSMFXGC4&utparam-url=scene%253Asearch%257Cquery_from%253A%257Cx_object_id%253A1005007117105334%257C_p_origin_prod%253A)|2|
|Slide switch|[Link](https://www.aliexpress.com/item/33013437240.html?spm=a2g0o.productlist.main.1.72627c356PTwN3&algo_pvid=3925e037-0fcc-4760-92b9-b75c4dfe0ff4&algo_exp_id=3925e037-0fcc-4760-92b9-b75c4dfe0ff4-0&pdp_ext_f=%257B%2522order%2522%253A%2522310%2522%252C%2522spu_best_type%2522%253A%2522order%2522%252C%2522eval%2522%253A%25221%2522%252C%2522fromPage%2522%253A%2522search%2522%257D&pdp_npi=6%2540dis%2521EUR%25210.51%25210.51%2521%2521%25210.58%25210.58%2521%2540210384b217692743994642910e4027%252112000052353931373%2521sea%2521HR%25216267174471%2521X%25211%25210%2521n_tag%253A-29919%253Bd%253Ae5d82de9%253Bm03_new_user%253A-29895&curPageLogUid=KtTWqbb8iwSd&utparam-url=scene%253Asearch%257Cquery_from%253A%257Cx_object_id%253A33013437240%257C_p_origin_prod%253A)|2|
|EVA foam (optional but recommended)|[Link](https://www.aliexpress.com/item/1005002621956105.html?spm=a2g0o.productlist.main.1.33687985BO7jgq&algo_pvid=5752a148-1d9d-4f2a-b611-1f8c2ef94a55&algo_exp_id=5752a148-1d9d-4f2a-b611-1f8c2ef94a55-0&pdp_ext_f=%257B%2522order%2522%253A%2522642%2522%252C%2522eval%2522%253A%25221%2522%252C%2522fromPage%2522%253A%2522search%2522%257D&pdp_npi=6%2540dis%2521EUR%25213.61%25213.61%2521%2521%25214.14%25214.14%2521%2540211b6a7a17692743777238346e3e24%252112000033456986498%2521sea%2521HR%25216267174471%2521X%25211%25210%2521n_tag%253A-29919%253Bd%253Ae5d82de9%253Bm03_new_user%253A-29895&curPageLogUid=reGzNZ3dRqrA&utparam-url=scene%253Asearch%257Cquery_from%253A%257Cx_object_id%253A1005002621956105%257C_p_origin_prod%253A)||
|JST battery connectors (optional but recommended)|[Link](https://www.aliexpress.com/item/1005003390942788.html?spm=a2g0o.productlist.main.1.5b953f16rAF4sw&algo_pvid=47df1bbe-6053-4ec5-b64c-d39449708bd4&algo_exp_id=47df1bbe-6053-4ec5-b64c-d39449708bd4-0&pdp_ext_f=%257B%2522order%2522%253A%25223746%2522%252C%2522eval%2522%253A%25221%2522%252C%2522fromPage%2522%253A%2522search%2522%257D&pdp_npi=6%2540dis%2521EUR%25211.73%25211.73%2521%2521%25211.99%25211.99%2521%2540211b653717692744573003541e78fe%252112000025564240283%2521sea%2521HR%25216267174471%2521X%25211%25210%2521n_tag%253A-29919%253Bd%253Ae5d82de9%253Bm03_new_user%253A-29895&curPageLogUid=SfgaTyrJlQpx&utparam-url=scene%253Asearch%257Cquery_from%253A%257Cx_object_id%253A1005003390942788%257C_p_origin_prod%253A)||

## 

## Build instructions

**For Wiring process reference Build Video:** [YouTube](https://www.youtube.com/watch?v=XWv2SwuP9wc)

### **Step 1:**  Prepare everything (Printed part and materials)

### **Step 2:** Put Hotswap sockets in the hotswap plate

### **Step 3**: Put together hotswap plate and switch plate, screw them using m2x10 screws and standoffs

### **Step 4:** Insert the switches

### **Step 5**: Insert and solder the diodes to the hotswap sockets, placing diodes in their place in the hotswap plate

### **Step 6:** Wire other legs of the diodes to create rows

### **Step 7:** Isolate the rows using kapton tape

### **Step 8:** Cut the copper wire for the columns and wire it to other hotswap contact

### **Step 9:** Wire rows and columns to the controller

### **Step 10:** Solder on/off switch with battery and the controller

### **Step 11:** Flash the firmware to the board and test it (Remember that right half wont work if the left is not running)

### **Step 12:** Insert controller into the case, add some hot glue to hold it into the place, insert switch in its socket and screw the bottom of the case to the plate using m2x4 screws

### **Step 13:** Add keycaps and glue the magnets to the case

### **Step 14:** Repeat the same for the other half and enjoy your new keyboard

