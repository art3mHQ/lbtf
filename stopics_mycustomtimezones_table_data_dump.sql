--
-- PostgreSQL database dump
--

-- Dumped from database version 13.2 (Debian 13.2-1.pgdg100+1)
-- Dumped by pg_dump version 13.2 (Debian 13.2-1.pgdg100+1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Data for Name: topics_mycustomtimezones; Type: TABLE DATA; Schema: public; Owner: debug
--

COPY public.topics_mycustomtimezones (id, timezone_char) FROM stdin;
440	Africa/Abidjan
441	Africa/Accra
442	Africa/Addis_Ababa
443	Africa/Algiers
444	Africa/Asmara
445	Africa/Bamako
446	Africa/Bangui
447	Africa/Banjul
448	Africa/Bissau
449	Africa/Blantyre
450	Africa/Brazzaville
451	Africa/Bujumbura
452	Africa/Cairo
453	Africa/Casablanca
454	Africa/Ceuta
455	Africa/Conakry
456	Africa/Dakar
457	Africa/Dar_es_Salaam
458	Africa/Djibouti
459	Africa/Douala
460	Africa/El_Aaiun
461	Africa/Freetown
462	Africa/Gaborone
463	Africa/Harare
464	Africa/Johannesburg
465	Africa/Juba
466	Africa/Kampala
467	Africa/Khartoum
468	Africa/Kigali
469	Africa/Kinshasa
470	Africa/Lagos
471	Africa/Libreville
472	Africa/Lome
473	Africa/Luanda
474	Africa/Lubumbashi
475	Africa/Lusaka
476	Africa/Malabo
477	Africa/Maputo
478	Africa/Maseru
479	Africa/Mbabane
480	Africa/Mogadishu
481	Africa/Monrovia
482	Africa/Nairobi
483	Africa/Ndjamena
484	Africa/Niamey
485	Africa/Nouakchott
486	Africa/Ouagadougou
487	Africa/Porto-Novo
488	Africa/Sao_Tome
489	Africa/Tripoli
490	Africa/Tunis
491	Africa/Windhoek
492	America/Adak
493	America/Anchorage
494	America/Anguilla
495	America/Antigua
496	America/Araguaina
497	America/Argentina/Buenos_Aires
498	America/Argentina/Catamarca
499	America/Argentina/Cordoba
500	America/Argentina/Jujuy
501	America/Argentina/La_Rioja
502	America/Argentina/Mendoza
503	America/Argentina/Rio_Gallegos
504	America/Argentina/Salta
505	America/Argentina/San_Juan
506	America/Argentina/San_Luis
507	America/Argentina/Tucuman
508	America/Argentina/Ushuaia
509	America/Aruba
510	America/Asuncion
511	America/Atikokan
512	America/Bahia
513	America/Bahia_Banderas
514	America/Barbados
515	America/Belem
516	America/Belize
517	America/Blanc-Sablon
518	America/Boa_Vista
519	America/Bogota
520	America/Boise
521	America/Cambridge_Bay
522	America/Campo_Grande
523	America/Cancun
524	America/Caracas
525	America/Cayenne
526	America/Cayman
527	America/Chicago
528	America/Chihuahua
529	America/Costa_Rica
530	America/Creston
531	America/Cuiaba
532	America/Curacao
533	America/Danmarkshavn
534	America/Dawson
535	America/Dawson_Creek
536	America/Denver
537	America/Detroit
538	America/Dominica
539	America/Edmonton
540	America/Eirunepe
541	America/El_Salvador
542	America/Fort_Nelson
543	America/Fortaleza
544	America/Glace_Bay
545	America/Goose_Bay
546	America/Grand_Turk
547	America/Grenada
548	America/Guadeloupe
549	America/Guatemala
550	America/Guayaquil
551	America/Guyana
552	America/Halifax
553	America/Havana
554	America/Hermosillo
555	America/Indiana/Indianapolis
556	America/Indiana/Knox
557	America/Indiana/Marengo
558	America/Indiana/Petersburg
559	America/Indiana/Tell_City
560	America/Indiana/Vevay
561	America/Indiana/Vincennes
562	America/Indiana/Winamac
563	America/Inuvik
564	America/Iqaluit
565	America/Jamaica
566	America/Juneau
567	America/Kentucky/Louisville
568	America/Kentucky/Monticello
569	America/Kralendijk
570	America/La_Paz
571	America/Lima
572	America/Los_Angeles
573	America/Lower_Princes
574	America/Maceio
575	America/Managua
576	America/Manaus
577	America/Marigot
578	America/Martinique
579	America/Matamoros
580	America/Mazatlan
581	America/Menominee
582	America/Merida
583	America/Metlakatla
584	America/Mexico_City
585	America/Miquelon
586	America/Moncton
587	America/Monterrey
588	America/Montevideo
589	America/Montserrat
590	America/Nassau
591	America/New_York
592	America/Nipigon
593	America/Nome
594	America/Noronha
595	America/North_Dakota/Beulah
596	America/North_Dakota/Center
597	America/North_Dakota/New_Salem
598	America/Nuuk
599	America/Ojinaga
600	America/Panama
601	America/Pangnirtung
602	America/Paramaribo
603	America/Phoenix
604	America/Port-au-Prince
605	America/Port_of_Spain
606	America/Porto_Velho
607	America/Puerto_Rico
608	America/Punta_Arenas
609	America/Rainy_River
610	America/Rankin_Inlet
611	America/Recife
612	America/Regina
613	America/Resolute
614	America/Rio_Branco
615	America/Santarem
616	America/Santiago
617	America/Santo_Domingo
618	America/Sao_Paulo
619	America/Scoresbysund
620	America/Sitka
621	America/St_Barthelemy
622	America/St_Johns
623	America/St_Kitts
624	America/St_Lucia
625	America/St_Thomas
626	America/St_Vincent
627	America/Swift_Current
628	America/Tegucigalpa
629	America/Thule
630	America/Thunder_Bay
631	America/Tijuana
632	America/Toronto
633	America/Tortola
634	America/Vancouver
635	America/Whitehorse
636	America/Winnipeg
637	America/Yakutat
638	America/Yellowknife
639	Antarctica/Casey
640	Antarctica/Davis
641	Antarctica/DumontDUrville
642	Antarctica/Macquarie
643	Antarctica/Mawson
644	Antarctica/McMurdo
645	Antarctica/Palmer
646	Antarctica/Rothera
647	Antarctica/Syowa
648	Antarctica/Troll
649	Antarctica/Vostok
650	Arctic/Longyearbyen
651	Asia/Aden
652	Asia/Almaty
653	Asia/Amman
654	Asia/Anadyr
655	Asia/Aqtau
656	Asia/Aqtobe
657	Asia/Ashgabat
658	Asia/Atyrau
659	Asia/Baghdad
660	Asia/Bahrain
661	Asia/Baku
662	Asia/Bangkok
663	Asia/Barnaul
664	Asia/Beirut
665	Asia/Bishkek
666	Asia/Brunei
667	Asia/Chita
668	Asia/Choibalsan
669	Asia/Colombo
670	Asia/Damascus
671	Asia/Dhaka
672	Asia/Dili
673	Asia/Dubai
674	Asia/Dushanbe
675	Asia/Famagusta
676	Asia/Gaza
677	Asia/Hebron
678	Asia/Ho_Chi_Minh
679	Asia/Hong_Kong
680	Asia/Hovd
681	Asia/Irkutsk
682	Asia/Jakarta
683	Asia/Jayapura
684	Asia/Jerusalem
685	Asia/Kabul
686	Asia/Kamchatka
687	Asia/Karachi
688	Asia/Kathmandu
689	Asia/Khandyga
690	Asia/Kolkata
691	Asia/Krasnoyarsk
692	Asia/Kuala_Lumpur
693	Asia/Kuching
694	Asia/Kuwait
695	Asia/Macau
696	Asia/Magadan
697	Asia/Makassar
698	Asia/Manila
699	Asia/Muscat
700	Asia/Nicosia
701	Asia/Novokuznetsk
702	Asia/Novosibirsk
703	Asia/Omsk
704	Asia/Oral
705	Asia/Phnom_Penh
706	Asia/Pontianak
707	Asia/Pyongyang
708	Asia/Qatar
709	Asia/Qostanay
710	Asia/Qyzylorda
711	Asia/Riyadh
712	Asia/Sakhalin
713	Asia/Samarkand
714	Asia/Seoul
715	Asia/Shanghai
716	Asia/Singapore
717	Asia/Srednekolymsk
718	Asia/Taipei
719	Asia/Tashkent
720	Asia/Tbilisi
721	Asia/Tehran
722	Asia/Thimphu
723	Asia/Tokyo
724	Asia/Tomsk
725	Asia/Ulaanbaatar
726	Asia/Urumqi
727	Asia/Ust-Nera
728	Asia/Vientiane
729	Asia/Vladivostok
730	Asia/Yakutsk
731	Asia/Yangon
732	Asia/Yekaterinburg
733	Asia/Yerevan
734	Atlantic/Azores
735	Atlantic/Bermuda
736	Atlantic/Canary
737	Atlantic/Cape_Verde
738	Atlantic/Faroe
739	Atlantic/Madeira
740	Atlantic/Reykjavik
741	Atlantic/South_Georgia
742	Atlantic/St_Helena
743	Atlantic/Stanley
744	Australia/Adelaide
745	Australia/Brisbane
746	Australia/Broken_Hill
747	Australia/Darwin
748	Australia/Eucla
749	Australia/Hobart
750	Australia/Lindeman
751	Australia/Lord_Howe
752	Australia/Melbourne
753	Australia/Perth
754	Australia/Sydney
755	Canada/Atlantic
756	Canada/Central
757	Canada/Eastern
758	Canada/Mountain
759	Canada/Newfoundland
760	Canada/Pacific
761	Europe/Amsterdam
762	Europe/Andorra
763	Europe/Astrakhan
764	Europe/Athens
765	Europe/Belgrade
766	Europe/Berlin
767	Europe/Bratislava
768	Europe/Brussels
769	Europe/Bucharest
770	Europe/Budapest
771	Europe/Busingen
772	Europe/Chisinau
773	Europe/Copenhagen
774	Europe/Dublin
775	Europe/Gibraltar
776	Europe/Guernsey
777	Europe/Helsinki
778	Europe/Isle_of_Man
779	Europe/Istanbul
780	Europe/Jersey
781	Europe/Kaliningrad
782	Europe/Kiev
783	Europe/Kirov
784	Europe/Lisbon
785	Europe/Ljubljana
786	Europe/London
787	Europe/Luxembourg
788	Europe/Madrid
789	Europe/Malta
790	Europe/Mariehamn
791	Europe/Minsk
792	Europe/Monaco
793	Europe/Moscow
794	Europe/Oslo
795	Europe/Paris
796	Europe/Podgorica
797	Europe/Prague
798	Europe/Riga
799	Europe/Rome
800	Europe/Samara
801	Europe/San_Marino
802	Europe/Sarajevo
803	Europe/Saratov
804	Europe/Simferopol
805	Europe/Skopje
806	Europe/Sofia
807	Europe/Stockholm
808	Europe/Tallinn
809	Europe/Tirane
810	Europe/Ulyanovsk
811	Europe/Uzhgorod
812	Europe/Vaduz
813	Europe/Vatican
814	Europe/Vienna
815	Europe/Vilnius
816	Europe/Volgograd
817	Europe/Warsaw
818	Europe/Zagreb
819	Europe/Zaporozhye
820	Europe/Zurich
821	GMT
822	Indian/Antananarivo
823	Indian/Chagos
824	Indian/Christmas
825	Indian/Cocos
826	Indian/Comoro
827	Indian/Kerguelen
828	Indian/Mahe
829	Indian/Maldives
830	Indian/Mauritius
831	Indian/Mayotte
832	Indian/Reunion
833	Pacific/Apia
834	Pacific/Auckland
835	Pacific/Bougainville
836	Pacific/Chatham
837	Pacific/Chuuk
838	Pacific/Easter
839	Pacific/Efate
840	Pacific/Enderbury
841	Pacific/Fakaofo
842	Pacific/Fiji
843	Pacific/Funafuti
844	Pacific/Galapagos
845	Pacific/Gambier
846	Pacific/Guadalcanal
847	Pacific/Guam
848	Pacific/Honolulu
849	Pacific/Kiritimati
850	Pacific/Kosrae
851	Pacific/Kwajalein
852	Pacific/Majuro
853	Pacific/Marquesas
854	Pacific/Midway
855	Pacific/Nauru
856	Pacific/Niue
857	Pacific/Norfolk
858	Pacific/Noumea
859	Pacific/Pago_Pago
860	Pacific/Palau
861	Pacific/Pitcairn
862	Pacific/Pohnpei
863	Pacific/Port_Moresby
864	Pacific/Rarotonga
865	Pacific/Saipan
866	Pacific/Tahiti
867	Pacific/Tarawa
868	Pacific/Tongatapu
869	Pacific/Wake
870	Pacific/Wallis
871	US/Alaska
872	US/Arizona
873	US/Central
874	US/Eastern
875	US/Hawaii
876	US/Mountain
877	US/Pacific
878	UTC
\.


--
-- Name: topics_mycustomtimezones_id_seq; Type: SEQUENCE SET; Schema: public; Owner: debug
--

SELECT pg_catalog.setval('public.topics_mycustomtimezones_id_seq', 878, true);


--
-- PostgreSQL database dump complete
--
