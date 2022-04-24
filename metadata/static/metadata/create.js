$(document).ready(function () {
    const createModal = document.getElementById('createModal')

    if (createModal) {
        $('#createModal').modal('show');
    }
})

// const element = $('#keywords');
// element.insertAfter($('#div_id_dataset_progress'));

// const metada_form = document.getElementById('metada_form')
// const keywords_input = document.getElementById('id_science_keywords')

// console.log(metada_form);
// metada_form.addEventListener("submit", (e) => {
//     e.preventDefault();

//     const default_keys = keywords_input.value;
//     console.log(default_keys);

//     const arr = $('#keywords').select2('data')
//     let result = []
//     for (const item of arr) {
//         result.push(item.id)
//     }
//     console.log(result.toString())
//     // metada_form.submit();
// });

// $('#keywords').select2({
//     placeholder: "Add or select keywords that describe the Scientific parameters...",
//     allowClear: true,
//     minimumInputLength: 3,
//     ajax:
//     {
//         url: "/search_science_keywords/",
//         dataType: 'json',
//         type: 'GET',
//         delay: 250,
//         data: function (params) {
//             return {
//                 search: params.term,
//             }
//         },

//         processResults: function (data) {
//             return {
//                 results: data
//             };
//         },

//         cache: true
//     },
// });