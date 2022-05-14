const csrf = document.getElementsByName('csrfmiddlewaretoken')[0].value
const alertBox = document.getElementById('alert-box')
const btn_continue = document.getElementById('btn-continue')


btn_continue.addEventListener('click', onContinue)
Dropzone.autoDiscover = false


const myDropzone = new Dropzone('#my-dropozne', {
    url: '/upload/',
    init: function () {
        this.on('sending', function (file, xhr, formData) {
            console.log('sending')
            formData.append('csrfmiddlewaretoken', csrf)
        })
        this.on('removedfile', function (file) {
            console.log('removedfile')
            if (myDropzone.files.length < 1) {
                btn_continue.setAttribute('disabled', "")
            }
        })
        this.on('addedfiles', function (files) {
            console.log('addedfiles')
            btn_continue.attributes.removeNamedItem('disabled')
        })
        this.on('successmultiple', function (files, response) {
            // myDropzone.reset();
            if (response.success) {
                console.log("Your files has been uploaded")
                handleAlerts('success', 'Your files has been uploaded')
                window.location.href = "/create/" + response.metadata_id
            } else {
                console.log("File already exists")
                handleAlerts('danger', 'File already exists')
            }
        })
    },
    maxFiles: 100,
    maxFilesize: 100,
    parallelUploads: 100,
    // uploadMultiple: true,
    addRemoveLinks: true,
    autoProcessQueue: false,
    // image/*,application/pdf,.psd
    acceptedFiles: '.csv,.xlsx'
})

function handleAlerts(type, msg) {
    alertBox.innerHTML = `
        <div class="alert alert-${type}" role="alert">
            ${msg}
        </div>
    `
}

function onContinue() {
    myDropzone.processQueue()
}