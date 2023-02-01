from django.db import models
from django.utils import timezone


class Author(models.Model):
    objects = None
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.full_name()


class Tour(models.Model):

    ok_awaria = [("Ok", 'Ok'), ("Awaria", 'Awaria')]
    zal_wyl = [("Zał.", 'Zał.'), ("Wył.", 'Wył.')]
    auto_lokal = [("Auto.", 'Auto.'), ("Lokal.", 'Lokal.')]
    inw_bat = [("Inwerter", "Inwerter"), ("Z baterii", "Z baterii"), ("Awaria", "Awaria")]
    ziel_czer = [("Zielone", "Zielone"), ("Czerwone", "Czerwone")]
    i_c = [("I", "I"), ("C", "C")]

    # summary
    objects = None
    date = models.DateField(default=timezone.now)
    author = models.ForeignKey(to=Author, null=True, on_delete=models.CASCADE, related_name="author")

    # TR 1.1
    tr11 = models.CharField(max_length=300, default='Trans TR1.1', null=True, blank=True)
    tr11_temp_A1 = models.IntegerField()
    tr11_temp_A2 = models.IntegerField()
    tr11_temp_A3 = models.IntegerField()
    tr11_notes = models.CharField(max_length=300, null=True, blank=True)

    # TR 1.2
    tr12 = models.CharField(max_length=300, default='Trans TR1.2', null=True, blank=True)
    tr12_temp_A1 = models.IntegerField()
    tr12_temp_A2 = models.IntegerField()
    tr12_temp_A3 = models.IntegerField()
    tr12_notes = models.CharField(max_length=300, null=True, blank=True)

    # TR 2.1
    tr21 = models.CharField(max_length=300, default='Trans TR2.1', null=True, blank=True)
    tr21_temp_A1 = models.IntegerField()
    tr21_temp_A2 = models.IntegerField()
    tr21_temp_A3 = models.IntegerField()
    tr21_notes = models.CharField(max_length=300, null=True, blank=True)

    # TR 3.1
    tr31 = models.CharField(max_length=300, default='Trans TR3.1', null=True, blank=True)
    tr31_temp_A1 = models.IntegerField()
    tr31_temp_A2 = models.IntegerField()
    tr31_temp_A3 = models.IntegerField()
    tr31_notes = models.CharField(max_length=300, null=True, blank=True)

    # TR 4.1
    tr41 = models.CharField(max_length=300, default='Trans TR4.1', null=True, blank=True)
    tr41_temp_A1 = models.IntegerField(default=0)
    tr41_temp_A2 = models.IntegerField(default=0)
    tr41_temp_A3 = models.IntegerField(default=0)
    tr41_notes = models.CharField(max_length=300, null=True, blank=True)

    # TR 4.2
    tr42 = models.CharField(max_length=300, default='Trans TR4.2', null=True, blank=True)
    tr42_temp_A1 = models.IntegerField(default=0)
    tr42_temp_A2 = models.IntegerField(default=0)
    tr42_temp_A3 = models.IntegerField(default=0)
    tr42_notes = models.CharField(max_length=300, null=True, blank=True)

    # SN pole nr 3 (odczyt z anal.)
    sn_field_3 = models.CharField(max_length=300, default='SN pole nr 3 (odczyt z anal.)', null=True, blank=True)
    sn_field_3_v12 = models.FloatField()
    sn_field_3_v23 = models.FloatField()
    sn_field_3_v31 = models.FloatField()
    sn_field_3_notes = models.CharField(max_length=300, null=True, blank=True)

    # SN pole nr 5 (odczyt z anal.)
    sn_field_5 = models.CharField(max_length=300, default='SN pole nr 5 (odczyt z anal.)', null=True, blank=True)
    sn_field_5_v12 = models.FloatField()
    sn_field_5_v23 = models.FloatField()
    sn_field_5_v31 = models.FloatField()
    sn_field_5_notes = models.CharField(max_length=300, null=True, blank=True)

    # SZR SN stan
    szr_sn_stan = models.CharField(max_length=300, default='SZR SN Stan', null=True, blank=True)
    breaker_3 = models.CharField(max_length=10, choices=zal_wyl, null=True, default="Zał.")
    breaker_4 = models.CharField(max_length=10, choices=zal_wyl, null=True, default="Wył.")
    breaker_5 = models.CharField(max_length=10, choices=zal_wyl, null=True, default="Zał.")
    szr_sn_stan_notes = models.CharField(max_length=300, null=True, blank=True)

    # SZR controling
    szr_controling = models.CharField(max_length=300, default='SZR Sterowanie', null=True, blank=True)
    controling = models.CharField(max_length=10, choices=auto_lokal, null=True, default="Auto.")
    szr_activity = models.CharField(max_length=10, choices=zal_wyl, null=True, default="Zał.")
    szr_blockade = models.CharField(max_length=10, choices=zal_wyl, null=True, default="Wył.")
    szr_controling_notes = models.CharField(max_length=300, null=True, blank=True)

    # SN pole nr 3 THDS U
    sn_field_3_thds = models.CharField(max_length=300, default='SN pole nr 3 THDS U', null=True, blank=True)
    sn_field_3_thds_v12 = models.FloatField()
    sn_field_3_thds_v23 = models.FloatField()
    sn_field_3_thds_v31 = models.FloatField()
    sn_field_3_thds_notes = models.CharField(max_length=300, null=True, blank=True)

    # SN pole nr 5 THDS U
    sn_field_5_thds = models.CharField(max_length=300, default='SN pole nr 5 THDS U', null=True, blank=True)
    sn_field_5_thds_v12 = models.FloatField()
    sn_field_5_thds_v23 = models.FloatField()
    sn_field_5_thds_v31 = models.FloatField()
    sn_field_5_thds_notes = models.CharField(max_length=300, null=True, blank=True)

    # SN pole nr 3 cos fi
    sn_field_3_cosfi = models.CharField(max_length=300, default='SN pole nr 3 cosΦ', null=True, blank=True)
    sn_field_3_cosfi_a = models.FloatField()
    sn_field_3_cosfi_b = models.FloatField()
    sn_field_3_cosfi_c = models.FloatField()
    sn_field_3_cosfi_notes = models.CharField(max_length=300, null=True, blank=True)

    # SN pole nr 5 cos fi
    sn_field_5_cosfi = models.CharField(max_length=300, default='SN pole nr 5 cosΦ', null=True, blank=True)
    sn_field_5_cosfi_a = models.FloatField()
    sn_field_5_cosfi_b = models.FloatField()
    sn_field_5_cosfi_c = models.FloatField()
    sn_field_5_cosfi_notes = models.CharField(max_length=300, null=True, blank=True)

    # Rozdz. 1.1 RG cos fi
    rozdz11_cosfi = models.CharField(max_length=300, default='Rozdz. 1.1RG', null=True, blank=True)
    rozdz11_cosfi_1 = models.FloatField()
    rozdz11_ind_1 = models.CharField(max_length=3, null=True, blank=True, choices=i_c)
    rozdz11_cosfi_2 = models.FloatField()
    rozdz11_ind_2 = models.CharField(max_length=3, null=True, blank=True, choices=i_c)
    rozdz11_cosfi_3 = models.FloatField()
    rozdz11_ind_3 = models.CharField(max_length=3, null=True, blank=True, choices=i_c)
    rozdz11_cosfi_notes = models.CharField(max_length=300, null=True, blank=True)

    # Rozdz. 1.2 RG cos fi
    rozdz12_cosfi = models.CharField(max_length=300, default='Rozdz. 1.2RG', null=True, blank=True)
    rozdz12_cosfi_1 = models.FloatField()
    rozdz12_ind_1 = models.CharField(max_length=3, null=True, blank=True, choices=i_c)
    rozdz12_cosfi_2 = models.FloatField()
    rozdz12_ind_2 = models.CharField(max_length=3, null=True, blank=True, choices=i_c)
    rozdz12_cosfi_3 = models.FloatField()
    rozdz12_ind_3 = models.CharField(max_length=3, null=True, blank=True, choices=i_c)
    rozdz12_cosfi_notes = models.CharField(max_length=300, null=True, blank=True)

    # Rozdz. 2.1 RG cos fi
    rozdz21_cosfi = models.CharField(max_length=300, default='Rozdz. 2.1RG', null=True, blank=True)
    rozdz21_cosfi_1 = models.FloatField()
    rozdz21_ind_1 = models.CharField(max_length=3, null=True, blank=True, choices=i_c)
    rozdz21_cosfi_2 = models.FloatField()
    rozdz21_ind_2 = models.CharField(max_length=3, null=True, blank=True, choices=i_c)
    rozdz21_cosfi_3 = models.FloatField()
    rozdz21_ind_3 = models.CharField(max_length=3, null=True, blank=True, choices=i_c)
    rozdz21_cosfi_notes = models.CharField(max_length=300, null=True, blank=True)

    # Rozdz. 3.1 RG cos fi
    rozdz31_cosfi = models.CharField(max_length=300, default='Rozdz. 3.1RG', null=True, blank=True)
    rozdz31_cosfi_1 = models.FloatField()
    rozdz31_ind_1 = models.CharField(max_length=3, null=True, blank=True, choices=i_c)
    rozdz31_cosfi_2 = models.FloatField()
    rozdz31_ind_2 = models.CharField(max_length=3, null=True, blank=True, choices=i_c)
    rozdz31_cosfi_3 = models.FloatField()
    rozdz31_ind_3 = models.CharField(max_length=3, null=True, blank=True, choices=i_c)
    rozdz31_cosfi_notes = models.CharField(max_length=300, null=True, blank=True)

    # UPSy 1.34
    ups_1_34 = models.CharField(max_length=300, default='UPS pom. 1.34 100kVA', null=True, blank=True)
    ups_1_34_l1 = models.IntegerField()
    ups_1_34_l2 = models.IntegerField()
    ups_1_34_l3 = models.IntegerField()
    ups_1_34_working_status = models.CharField(max_length=20, choices=inw_bat, default="Inwerter")
    ups_1_34_battery_voltages = models.IntegerField(default=272)
    ups_1_34_failures = models.CharField(max_length=100, default='brak')
    ups_1_34_working_temp = models.FloatField()
    ups_1_34_cooling_fans = models.CharField(max_length=10, choices=ok_awaria, null=True, default="Ok")
    ups_1_34_notes = models.CharField(max_length=300, null=True, blank=True)

    # UPSy tt
    ups_tt = models.CharField(max_length=300, default='UPS tunel tech. 40kVA', null=True, blank=True)
    ups_tt_l1 = models.IntegerField()
    ups_tt_l2 = models.IntegerField()
    ups_tt_l3 = models.IntegerField()
    ups_tt_working_status = models.CharField(max_length=20, choices=inw_bat, default="Inwerter")
    ups_tt_battery_voltages = models.IntegerField(default=272)
    ups_tt_failures = models.CharField(max_length=100, default='brak')
    ups_tt_working_temp = models.FloatField()
    ups_tt_cooling_fans = models.CharField(max_length=10, choices=ok_awaria, null=True, default="ONE")
    ups_tt_notes = models.CharField(max_length=300, null=True, blank=True)

    # UPSy GPD
    ups_GPD = models.CharField(max_length=300, default='UPS GPD 80kVA', null=True, blank=True)
    ups_GPD_l1 = models.IntegerField()
    ups_GPD_l2 = models.IntegerField()
    ups_GPD_l3 = models.IntegerField()
    ups_GPD_working_status = models.CharField(max_length=20, choices=inw_bat, default="Inwerter")
    ups_GPD_battery_voltages = models.IntegerField(default=272)
    ups_GPD_failures = models.CharField(max_length=100, default='brak')
    ups_GPD_working_temp = models.FloatField()
    ups_GPD_cooling_fans = models.CharField(max_length=10, choices=ok_awaria, null=True, default='Ok')
    ups_GPD_notes = models.CharField(max_length=300, null=True, blank=True)

    # UPSy BL-04BM
    ups_BL04BM = models.CharField(max_length=300, default='UPS BL04BM 15kVA', null=True, blank=True)
    ups_BL04BM_l1 = models.IntegerField()
    ups_BL04BM_l2 = models.IntegerField()
    ups_BL04BM_l3 = models.IntegerField()
    ups_BL04BM_working_status = models.CharField(max_length=20, choices=inw_bat, default="Inwerter")
    ups_BL04BM_battery_voltages = models.IntegerField(default=272)
    ups_BL04BM_failures = models.CharField(max_length=100, default='brak')
    ups_BL04BM_working_temp = models.FloatField()
    ups_BL04BM_cooling_fans = models.CharField(max_length=10, choices=ok_awaria, null=True, default="Ok")
    ups_BL04BM_notes = models.CharField(max_length=300, null=True, blank=True)

    # UPSy BL-06ID
    ups_BL06ID = models.CharField(max_length=300, default='UPS BL06ID 15kVA', null=True, blank=True)
    ups_BL06ID_l1 = models.IntegerField()
    ups_BL06ID_l2 = models.IntegerField()
    ups_BL06ID_l3 = models.IntegerField()
    ups_BL06ID_working_status = models.CharField(max_length=20, choices=inw_bat, default="Inwerter")
    ups_BL06ID_battery_voltages = models.IntegerField(default=272)
    ups_BL06ID_failures = models.CharField(max_length=100, default='brak')
    ups_BL06ID_working_temp = models.FloatField()
    ups_BL06ID_cooling_fans = models.CharField(max_length=10, choices=ok_awaria, null=True, default="Ok")
    ups_BL06ID_notes = models.CharField(max_length=300, null=True, blank=True)

    # UPSy BL04ID
    ups_BL04ID = models.CharField(max_length=300, default='UPS BL04ID 20kVA', null=True, blank=True)
    ups_BL04ID_l1 = models.IntegerField()
    ups_BL04ID_l2 = models.IntegerField()
    ups_BL04ID_l3 = models.IntegerField()
    ups_BL04ID_working_status = models.CharField(max_length=20, choices=inw_bat, default="Inwerter")
    ups_BL04ID_battery_voltages = models.IntegerField(default=272)
    ups_BL04ID_failures = models.CharField(max_length=100, default='brak')
    ups_BL04ID_working_temp = models.FloatField()
    ups_BL04ID_cooling_fans = models.CharField(max_length=10, choices=ok_awaria, null=True, default="Ok")
    ups_BL04ID_notes = models.CharField(max_length=300, null=True, blank=True)

    # UPSy BL10BM
    ups_BL10BM = models.CharField(max_length=300, default='UPS BL10BM 12kVA', null=True, blank=True)
    ups_BL10BM_l1 = models.IntegerField()
    ups_BL10BM_l2 = models.IntegerField()
    ups_BL10BM_l3 = models.IntegerField()
    ups_BL10BM_working_status = models.CharField(max_length=20, choices=inw_bat, default="Inwerter")
    ups_BL10BM_battery_voltages = models.IntegerField(default=272)
    ups_BL10BM_failures = models.CharField(max_length=100, default='brak')
    ups_BL10BM_working_temp = models.FloatField()
    ups_BL10BM_cooling_fans = models.CharField(max_length=10, choices=ok_awaria, null=True, default="Ok")
    ups_BL10BM_notes = models.CharField(max_length=300, null=True, blank=True)

    # UPSy BL09BM
    ups_BL09BM = models.CharField(max_length=300, default='UPS BL09BM 20kVA', null=True, blank=True)
    ups_BL09BM_l1 = models.IntegerField()
    ups_BL09BM_l2 = models.IntegerField()
    ups_BL09BM_l3 = models.IntegerField()
    ups_BL09BM_working_status = models.CharField(max_length=20, choices=inw_bat, default="Inwerter")
    ups_BL09BM_battery_voltages = models.IntegerField(default=272)
    ups_BL09BM_failures = models.CharField(max_length=100, default='brak')
    ups_BL09BM_working_temp = models.FloatField()
    ups_BL09BM_cooling_fans = models.CharField(max_length=10, choices=ok_awaria, null=True, default="Ok")
    ups_BL09BM_notes = models.CharField(max_length=300, null=True, blank=True)

    # UPSy omega BL05ID
    ups_BL05ID = models.CharField(max_length=300, default='UPS BL05ID 6kVA', null=True, blank=True)
    ups_BL05ID_load = models.IntegerField()
    ups_BL05ID_working_status = models.CharField(max_length=20, choices=inw_bat, default="Inwerter")
    ups_BL05ID_battery_voltages = models.IntegerField(default=242)
    ups_BL05ID_failures = models.CharField(max_length=100, default='brak')
    ups_BL05ID_working_temp = models.FloatField()
    ups_BL05ID_cooling_fans = models.CharField(max_length=10, choices=ok_awaria, null=True, default="Ok")
    ups_BL05ID_notes = models.CharField(max_length=300, null=True, blank=True)

    # UPSy omega PPOŻ
    ups_PPOZ = models.CharField(max_length=300, default='UPS P.POŻ pom 1.34 6kVA', null=True, blank=True)
    ups_PPOZ_load = models.IntegerField(default=0)
    ups_PPOZ_working_status = models.CharField(max_length=20, choices=inw_bat, default="Inwerter")
    ups_PPOZ_battery_voltages = models.IntegerField(default=242)
    ups_PPOZ_failures = models.CharField(max_length=100, default='brak')
    ups_PPOZ_working_temp = models.FloatField()
    ups_PPOZ_cooling_fans = models.CharField(max_length=10, choices=ok_awaria, null=True, default="Ok")
    ups_PPOZ_notes = models.CharField(max_length=300, null=True, blank=True)

    # Bateria kondensatorów S1-1.1RG
    bat11 = models.CharField(max_length=300, default='S1-1.1RG Bateria kondensatorów', null=True, blank=True)
    bat11_temp = models.FloatField()
    bat11_weekly_TPF = models.CharField(max_length=300)
    bat11_working_status = models.CharField(max_length=10, choices=auto_lokal, null=True, default="Auto.")
    bat11_notes = models.CharField(max_length=300, null=True, blank=True)

    # Bateria kondensatorów S1-1.2RG
    bat12 = models.CharField(max_length=300, default='S1-1.2RG Bateria kondensatorów', null=True, blank=True)
    bat12_temp = models.FloatField()
    bat12_weekly_TPF = models.CharField(max_length=300)
    bat12_working_status = models.CharField(max_length=10, choices=auto_lokal, null=True, default="Auto.")
    bat12_notes = models.CharField(max_length=300, null=True, blank=True)

    # Bateria kondensatorów S1-2.1RG
    bat21 = models.CharField(max_length=300, default='S1-2.1RG Bateria kondensatorów', null=True, blank=True)
    bat21_temp = models.FloatField()
    bat21_weekly_TPF = models.CharField(max_length=300)
    bat21_working_status = models.CharField(max_length=10, choices=auto_lokal, null=True, default="Auto.")
    bat21_notes = models.CharField(max_length=300, null=True, blank=True)

    # Bateria kondensatorów S1-3.1RG
    bat31 = models.CharField(max_length=300, default='S1-3.1RG Bateria kondensatorów', null=True, blank=True)
    bat31_temp = models.FloatField()
    bat31_weekly_TPF = models.CharField(max_length=300)
    bat31_working_status = models.CharField(max_length=10, choices=auto_lokal, null=True, default="Auto.")
    bat31_notes = models.CharField(max_length=300, null=True, blank=True)

    # Central battery
    central_battery = models.CharField(
        max_length=300, default='Centralna Bateria Oświetleniea aw.', null=True, blank=True)
    battery_voltages = models.FloatField()
    mains_charge = models.CharField(max_length=300, default="Zielone")
    bswok_charger = models.CharField(max_length=300, default="Zielone")
    central_battery_notes = models.CharField(max_length=300, null=True, blank=True)

    # Rozdz_RGE_AC
    rozdz_rge_ac = models.CharField(max_length=300, default='Rozdzielnica RGE-A,C', null=True, blank=True)
    rozdz_rge_ac_supply_tor_1 = models.IntegerField()
    rozdz_rge_ac_supply_tor_2 = models.IntegerField()
    szr_nn = models.CharField(max_length=10, choices=auto_lokal, null=True, default="Auto.")
    rozdz_rge_ac_notes = models.CharField(max_length=300, null=True, blank=True)

    # Active_filter
    active_filter = models.CharField(max_length=300, default='Aktywny Filtr tunel tech.', null=True, blank=True)
    working_status = models.CharField(
        max_length=100, choices=[("Standing by", 'Standing by'), ("??", '??')], null=True, default="Standing by")
    failures = models.CharField(max_length=300, default='Brak')
    thd_u = models.CharField(max_length=30, default="-")
    active_filter_notes = models.CharField(max_length=300, null=True, blank=True)

    # Emergency_lighting
    el = models.CharField(max_length=300, default='Oświetlenie awaryjne - Portiernia', null=True, blank=True)
    luminaire_number = models.CharField(max_length=30)
    error_type = models.CharField(max_length=300)
    lamp_status = models.CharField(max_length=300, choices=ziel_czer, default="Zielone")
    el_notes = models.CharField(max_length=300, null=True, blank=True)

    # Signaling_transformers_overheating
    sto = models.CharField(max_length=300, default='Syngalizacja przegrzania transformatorów', null=True, blank=True)
    lamp_status_concierge = models.CharField(max_length=10, choices=zal_wyl, null=True, default="Wył.")
    lamp_status_RaRTxx = models.CharField(max_length=10, choices=zal_wyl, null=True, default="Wył.")
    sto_notes = models.CharField(max_length=300, null=True, blank=True)

    # Rozdz_1.1RG_THD
    rg11_thd = models.CharField(max_length=300, default='Rozdz. 1.1RG', null=True, blank=True)
    rg11_thd_u = models.CharField(max_length=300)
    rg11_thd_i = models.CharField(max_length=300)
    rg11_thd_notes = models.CharField(max_length=300, null=True, blank=True)

    # Rozdz_1.2RG_THD
    rg12_thd = models.CharField(max_length=300, default='Rozdz. 1.2RG', null=True, blank=True)
    rg12_thd_u = models.CharField(max_length=300)
    rg12_thd_i = models.CharField(max_length=300)
    rg12_thd_notes = models.CharField(max_length=300, null=True, blank=True)

    # Rozdz_2.1RG_THD
    rg21_thd = models.CharField(max_length=300, default='Rozdz. 2.1RG', null=True, blank=True)
    rg21_thd_u = models.CharField(max_length=300)
    rg21_thd_i = models.CharField(max_length=300)
    rg21_thd_notes = models.CharField(max_length=300, null=True, blank=True)

    # Rozdz_3.1RG_THD
    rg31_thd = models.CharField(max_length=300, default='Rozdz. 3.1RG', null=True, blank=True)
    rg31_thd_u = models.CharField(max_length=300)
    rg31_thd_i = models.CharField(max_length=300)
    rg31_thd_notes = models.CharField(max_length=300, null=True, blank=True)

    # Power_supply_to_the_fire_protection_switch
    indicator = models.CharField(max_length=300, null=True, blank=True)
    voltage_indicator = models.CharField(max_length=10, choices=ok_awaria, null=True, default="Ok")
    indicator_notes = models.CharField(max_length=300, null=True, blank=True)

    def __str__(self):
        return f"{self.date} {self.author}"