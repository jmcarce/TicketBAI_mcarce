import xmlschema
my_schema = xmlschema.XMLSchema('fuentes/TicketBai-V1-2.xsd')
if not( my_schema.is_valid('fuentes/Ejemplo_TicketBAI_B00000034_B2022_0101.xml')):
    print('yepaaaa')

if ( my_schema.is_valid('fuentes/Ejemplo_TicketBAI_B00000034_B2022_0101.xml')):
    print('yesss is valid!')

my_schema.validate('fuentes/Ejemplo_TicketBAI_B00000034_B2022_0101.xml')

if not (my_schema.validate('fuentes/Ejemplo_TicketBAI_B00000034_B2022_0101.xml')):
    print('yupiiii')