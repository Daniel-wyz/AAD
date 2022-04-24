$(document).ready(function () {
    const createModal = document.getElementById('createModal')

    if (createModal) {
        $('#createModal').modal('show');
    }
})

const element = $('#keyword_selection');
element.insertAfter($('#div_id_dataset_progress'));

const metada_form = document.getElementById('metada_form')
const default_keywords_input = document.getElementById('default_keywords')
const default_keywords = default_keywords_input.value.split(";")

console.log(default_keywords)

// metada_form.addEventListener("submit", (e) => {
//     e.preventDefault();
//     metada_form.submit();
// });

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

default_keywords.forEach((item, index, array) => {
    if (item) {
        arr = item.split("-");
        const newOption = new Option(arr[1], arr[0], true, true);
        $('#keywords').append(newOption)
    }
});
$('#keywords').trigger('change');