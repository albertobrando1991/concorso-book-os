//Funzione per recuperare i bandi
function getBandi(url, body, callback) {
    var xhr = new XMLHttpRequest();
    xhr.open('POST', url, true);
    xhr.setRequestHeader('Accept', 'application/json, text/plain, */*');
    xhr.setRequestHeader('Access-Control-Allow-Origin', '*');
    xhr.setRequestHeader('Content-Type', 'application/json');

    xhr.onload = function() {
        if (xhr.status == 200) {
            callback(null, xhr.response);
        } else {
            callback(xhr.status);
        }
    };
    xhr.send(JSON.stringify(body));
}

//Funzione per mappare le label delle categorie concorsi
function dro_get_bandi_categories_label(key){
    const categoria = [];
    key = key.trim();
    categoria['Concorso'] = 'Concorso';
    categoria['Selezione Professionisti ed Esperti'] = 'Selezione Professionisti ed Esperti';
    categoria['Concorsi DFP – Formez Pa'] = 'Concorsi DFP – Formez Pa';
    categoria['Avvisi di mobilità'] = 'Avvisi di mobilità';
    categoria['Scelta PA/sede'] = 'Scelta PA/sede';
    categoria['Procedure Straordinarie'] = 'Procedure Straordinarie';
    categoria['Bando Apprendistato'] = 'Bando Apprendistato';
    categoria['Avviso OIV'] = 'Avvisi OIV';

    return categoria[key];
}

//Funzione per mappare le tipologie di valutazione concorsi
function dro_get_valutazione(key){
    const valutazioni = [];
    valutazioni['TITOLI'] = 'Per titoli';
    valutazioni['ESAMI'] = 'Per esami';
    valutazioni['COLLOQUIO'] = 'Per colloquio';
    valutazioni['TITOLI_ESAMI'] = 'Per titoli ed esami';
    valutazioni['TITOLI_COLLOQUIO'] = 'Per titoli e colloquio';
    valutazioni['CORSO_CONCORSO'] = 'Per corso-concorso';
    valutazioni['PROVE_ACCERTAMENTO_PROFES'] = 'Per selezione mediante lo svolgimento di prove volte all\'accertamento della professionalità richiesta';

    return valutazioni[key];
}

//Funzione per mostrare i bandi nella ricerca
function droRenderBandi(arrayBandi, formatBando) {
    var listaBandi = '';
    var addBandoCompact = item => listaBandi += `
        <div class="pb-3 mb-3">
            <p>${dro_convert_date(item.dataPubblicazione)}</p>
            <h3><a href="/bandi-e-avvisi/dettaglio-bando-avviso/?concorso_id=${item.id}">${item.titolo}</a></h3>
        </div>`;

    var addBandoFull = item => {
        var sedi_list = item.sedi.length == 0 ? 'Non specificata' : item.sedi.join(', ');
        var valutazione_list = '';

        if (item.tipiProcedureGruppo) {
            valutazione_list = item.tipiProcedureGruppo.map(dro_get_valutazione).join(', ');
        } else {
            valutazione_list = dro_get_valutazione(item.tipoProcedura);
        }

        var titolo_bando = HtmlSanitizer.SanitizeHtml(item.titolo);
        var descrizione_bando = HtmlSanitizer.SanitizeHtml(item.descrizioneBreve) || ' - ';
        var entiRiferimento = HtmlSanitizer.SanitizeHtml(item.entiRiferimento.join(', ')) || ' - ';

        listaBandi += `
            <div class="p-3 mb-3 border-bottom">
                <p class="h5 bando-title"><img src="/wp-content/plugins/dro-dashboard/assets/img/icona-ultimi-bandi-formez-portale-del-reclutamento.svg" alt="Icona risultato di ricerca" class="me-2"><a href="/bandi-e-avvisi/dettaglio-bando-avviso/?concorso_id=${item.id}" title="Leggi i dettagli di: `+titolo_bando+`" aria-label="Leggi i dettagli di: `+titolo_bando+`">${titolo_bando}</a></p>
                <p class="mb-2"><span class="concorso-label fw-bold">Descrizione: </span><div class="concorso-content concorso-short-desc text-break font-lora">${descrizione_bando}</div></p>
                <p class="mb-2"><span class="concorso-label fw-bold">Ente di riferimento: </span><span class="concorso-content font-lora">${entiRiferimento}</span></p>
                <p class="mb-2"><span class="concorso-label fw-bold">Area geografica: </span><span class="concorso-content font-lora">${sedi_list}</span></p>
                <p class="mb-2"><span class="concorso-label fw-bold">Valutazione: </span><span class="concorso-content font-lora">${valutazione_list}</span></p>
                <p class="mb-2"><span class="concorso-label fw-bold">Stato: </span><span class="${item.statusLabel} px-2 br-5 concorso-status"><strong class="font-titillium text-uppercase">${item.statusLabel}</strong></span></p>
                <p class="mb-2"><span class="concorso-label fw-bold">Data apertura candidature: </span><span class="concorso-content font-lora">${dro_convert_date(item.dataPubblicazione, true)}</span></p>
                <p class="mb-2"><span class="concorso-label fw-bold">Data chiusura candidature: </span><span class="concorso-content font-lora">${dro_convert_date(item.dataScadenza, true)}</span></p>
            </div>`;
    };

    if (formatBando === 'compact') {
        arrayBandi.forEach(addBandoCompact);
    } else if (formatBando === 'full') {
        if (arrayBandi.length > 0) {
            arrayBandi.forEach(addBandoFull);
        } else {
            listaBandi += '<div class="p-3 mb-3 border-bottom"><h3>Spiacenti, nessun risultato</h3></div>';
        }
    }

    return listaBandi;
}
