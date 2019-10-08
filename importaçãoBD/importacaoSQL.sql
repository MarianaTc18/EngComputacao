SELECT* FROM importcsv;

describe importcsv;

drop table importcsv;


CREATE TABLE importcsv(
				Hora VARCHAR(255),
                Nome_Completo VARCHAR(255) , 
                Contexto_do_Evento VARCHAR(255), 
                Componente VARCHAR(255),
                Nome_do_evento VARCHAR(255));