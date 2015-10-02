var notes = {
    '1': {
            'name': 'dfjghdkfg',
            'priority': '121',
            'content': 'fkdjgh;ethyoriyuoujapoefkjhrtkluesoirgjkhjkfsrfaksj',
        },
    '2': {
            'name': 'dfjgheiurn',
            'priority': '54',
            'content': 'isrhdtueytehgkdjfhgkjchgauywetrpwtre8yuodeg',
        },
};
var idForEdit = 0;

function updateData(){

    $('#resTable').empty();
    for(key in notes){
        var o = notes[key];
        o['id'] = key;
          $('#note_template').tmpl(o).appendTo('#resTable');
    }
    localStorage.setItem("notes", JSON.stringify(notes));
};

$(function (){
    var notes_tmp = localStorage.getItem("notes");
    if(notes_tmp != null){
        notes = JSON.parse(notes_tmp);
    }
    updateData();

    $('#addForm').submit(function (e){
        e.preventDefault();
        addNewNote();
        idForEdit = 0;
    });
});


function deleteItem(id){
    delete notes[id];
    updateData();
};


function addNewNote(){
    var newItem = {
        'name': $('#newName').val(),
        'priority': $('#newPriority').val(),
        'content': $('#newContent').val(),
    };
    if(newItem.name != "" && newItem.priority != "" && newItem.content != ""){
        if(idForEdit != 0){
            notes[idForEdit] = newItem;
            updateData();
        }else{
            id = Math.floor(Math.random() * (120 - 1)) + 1;
            notes[id] = newItem;
            updateData();
        }
    }else {
            alert("!!!Check data!!!");
        }

};

function editThisNote(id){
    idForEdit = id;
    $('#newName').val(notes[id]['name']);
    $('#newPriority').val(notes[id]['priority']);
    $('#newContent').val(notes[id]['content']);
};