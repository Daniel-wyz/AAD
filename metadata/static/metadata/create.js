const element = $('#keyword_selection');
element.insertAfter($('#div_id_dataset_progress'));

const metada_form = document.getElementById('metada_form')
const hitcount = document.getElementById('hitcount')

const columns = $("input[id^=column-]");
columns.on('change', (e) => {
    filter_keywords();
})
hitcount.addEventListener('change', (e) => {
    filter_keywords();
})

async function filter_keywords() {
    const metadata_id = metada_form.getAttribute("data");
    const count = hitcount.value;

    let url = `/filter_science_keywords/?metadata_id=${metadata_id}&hitcount=${count}`
    for (let column of columns) {
        if (!column.checked) {
            const label = column.getAttribute("data")
            url += `&excludes=${label}`
        }
    }
    console.log(url)

    const response = await fetch(url);
    const data = await response.json();
    fill_keywords(data);
}

function fill_keywords(keywords) {
    $('#keywords').val(null).trigger('change');

    keywords.forEach((item, index, array) => {
        if (item) {
            arr = item.split("-");
            const newOption = new Option(arr[1], arr[0], true, true);
            $('#keywords').append(newOption)
        }
    });
    $('#keywords').trigger('change');
}

$(document).ready(function () {
    filter_keywords();

    const createModal = document.getElementById('createModal')

    if (createModal) {
        $('#createModal').modal('show');
    }

    $('#keywords').select2({
        placeholder: "Add or select keywords that describe the Scientific parameters...",
        allowClear: true,
        minimumInputLength: 3,
        ajax:
        {
            url: "/search_science_keywords/",
            dataType: 'json',
            type: 'GET',
            delay: 250,
            data: function (params) {
                return {
                    search: params.term,
                }
            },

            processResults: function (data) {
                return {
                    results: data
                };
            },

            cache: true
        },
    });
})