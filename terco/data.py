# terco/data.py

ORATIONS = {
    "credo": {
        "titulo": "Credo",
        "texto": """Creio em Deus Pai todo-poderoso,
        criador do céu e da terra;
        e em Jesus Cristo, seu único Filho, nosso Senhor,
        que foi concebido pelo poder do Espírito Santo,
        nasceu da Virgem Maria,
        padeceu sob Pôncio Pilatos,
        foi crucificado, morto e sepultado;
        desceu à mansão dos mortos;
        ressuscitou ao terceiro dia;
        subiu aos céus;
        está sentado à direita de Deus Pai todo-poderoso,
        de onde há de vir a julgar os vivos e os mortos.
        Creio no Espírito Santo,
        na santa Igreja Católica,
        na comunhão dos santos,
        na remissão dos pecados,
        na ressurreição da carne,
        na vida eterna.
        Amém."""
    },
    "pai_nosso": {
        "titulo": "Pai Nosso",
        "texto": """Pai nosso, que estais nos céus,
        santificado seja o vosso nome;
        venha a nós o vosso reino;
        seja feita a vossa vontade,
        assim na terra como no céu.
        O pão nosso de cada dia nos dai hoje;
        perdoai-nos as nossas ofensas,
        assim como nós perdoamos a quem nos tem ofendido;
        e não nos deixeis cair em tentação,
        mas livrai-nos do mal.
        Amém."""
    },
    "ave_maria": {
        "titulo": "Ave Maria",
        "texto": """Ave Maria, cheia de graça,
        o Senhor é convosco,
        bendita sois vós entre as mulheres
        e bendito é o fruto do vosso ventre, Jesus.
        Santa Maria, Mãe de Deus,
        rogai por nós, pecadores,
        agora e na hora de nossa morte.
        Amém."""
    },
    "gloria_ao_pai": {
        "titulo": "Glória ao Pai",
        "texto": """Glória ao Pai, ao Filho e ao Espírito Santo.
        Assim como era no princípio, agora e sempre.
        Amém."""
    },
    "oracao_de_fatima": {
        "titulo": "Oração de Fátima",
        "texto": """Ó meu Jesus, perdoai-nos,
        livrai-nos do fogo do inferno,
        levai as almas todas para o Céu
        e socorrei principalmente as que mais precisarem."""
    },
    "salve_rainha": {
        "titulo": "Salve Rainha",
        "texto": """Salve Rainha, Mãe de misericórdia,
        vida, doçura e esperança nossa, salve!
        A vós bradamos, os degredados filhos de Eva;
        a vós suspiramos, gemendo e chorando neste vale de lágrimas.
        Eia, pois, advogada nossa,
        esses vossos olhos misericordiosos a nós volvei;
        e depois deste desterro, mostrai-nos Jesus,
        bendito fruto do vosso ventre,
        ó clemente, ó piedosa, ó doce sempre Virgem Maria.
        Rogai por nós, santa Mãe de Deus,
        para que sejamos dignos das promessas de Cristo.
        Amém."""
    }
}

MYSTERIES = {
    "gozosos": {
        "titulo": "Mistérios Gozosos (ou da Alegria)",
        "dias": ["segunda", "sábado"],
        "misterios": [
            "A Anunciação do Anjo Gabriel a Nossa Senhora.",
            "A Visitação de Nossa Senhora a Santa Isabel.",
            "O Nascimento de Jesus no presépio de Belém.",
            "A Apresentação do Menino Jesus no Templo.",
            "O Encontro do Menino Jesus no Templo."
        ]
    },
    "luminosos": {
        "titulo": "Mistérios Luminosos (ou da Luz)",
        "dias": ["quinta"],
        "misterios": [
            "O Batismo de Jesus no Jordão.",
            "A Revelação de Jesus nas Bodas de Caná.",
            "O Anúncio do Reino de Deus e o convite à conversão.",
            "A Transfiguração de Jesus no Monte Tabor.",
            "A Instituição da Eucaristia."
        ]
    },
    "dolorosos": {
        "titulo": "Mistérios Dolorosos (ou da Dor)",
        "dias": ["terça", "sexta"],
        "misterios": [
            "A Agonia de Jesus no Horto das Oliveiras.",
            "A Flagelação de Jesus atado à coluna.",
            "A Coroação de espinhos de Jesus.",
            "Jesus carregando a Cruz para o Calvário.",
            "A Crucifixão e Morte de Jesus na Cruz."
        ]
    },
    "gloriosos": {
        "titulo": "Mistérios Gloriosos (ou da Glória)",
        "dias": ["quarta", "domingo"],
        "misterios": [
            "A Ressurreição de Nosso Senhor Jesus Cristo.",
            "A Ascensão de Nosso Senhor Jesus Cristo ao Céu.",
            "A Vinda do Espírito Santo sobre os Apóstolos.",
            "A Assunção de Nossa Senhora ao Céu.",
            "A Coroação de Nossa Senhora como Rainha do Céu e da Terra."
        ]
    }
}