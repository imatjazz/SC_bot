###################### Tile views ###########################################
def more_info_ASA700(context):
    template = 'tiles/ASA_table.html'
    title = 'ASA Tables'
    args = [
        {'standard': 'ASA 700', 
        'example':'Public and large pty reporting entities, other entities using GP framework', 
        'applicableManuals': 'KAM, Australian Standard Reports Manual',
        'engagementToolLocation': 'Public & Large Pty, Regulatory/MIS/Financial reports'
        },
        {'standard': 'ASA 800', 
        'example':'Public and large pty reporting entities, other entities using GP framework', 
        'applicableManuals': 'KAM, Australian Standard Reports Manual',
        'engagementToolLocation': 'Public & Large Pty, Regulatory/MIS/Financial reports'
        }
    ]
    return [title, template, args]

def more_info_assurance_type(context):
    template = 'tiles/more_info.html'
    title = 'Reasonable vs Limited Assurance Engagement'
    args = [
        {'Assurance Type': 'Reasonable', 
        'example':'Public and large pty reporting entities, other entities using GP framework', 
        'applicableManuals': 'KAM, Australian Standard Reports Manual',
        'engagementToolLocation': 'Public & Large Pty, Regulatory/MIS/Financial reports'
        },
        {'Assurance Type': 'Limited', 
        'example':'Public and large pty reporting entities, other entities using GP framework', 
        'applicableManuals': 'KAM, Australian Standard Reports Manual',
        'engagementToolLocation': 'Public & Large Pty, Regulatory/MIS/Financial reports'
        }
    ]
    return [title, template, args]

###################### Tile index
TILES_INDEX = {
    'node_1_1521069602168' : [more_info_assurance_type],
    'node_1_1520902465516': [more_info_ASA700]
}
