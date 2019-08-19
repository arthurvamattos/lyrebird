let aberto = false;
let sideAtiva = ''
const sidebar = document.getElementById('sidebar');
const sidebarRight = document.getElementById('sidebar-right');
const content = document.getElementById('content');

let sidebarWidth = '250px'
const abrirmenu = () => {
    if (aberto){                
        if (window.innerWidth < 770) {
            sidebarRight.style.right = `-${sidebarWidth}`;
        } else {
            sidebar.style.left = `-${sidebarWidth}`;
        }
        content.style.width = '100%'
        aberto = false;
    } else { 
        if (window.innerWidth < 770) {
            sideAtiva = 'right'
            sidebarRight.style.right = '0';
        } else {
            sideAtiva = 'left'
            sidebar.style.left = '0';
        }               
        content.style.width = `calc(100% - ${sidebarWidth}`;        
        aberto = true;
    }
}

window.onresize = () => {
    if (aberto) {
        if (window.innerWidth < 770 && sideAtiva === 'left') {
            sidebar.style.left = `-${sidebarWidth}`;
            sidebarRight.style.right = '0';
            sideAtiva = 'right'
        } else if (window.innerWidth > 770 && sideAtiva === 'right') {
            sidebar.style.left = '0';
            sidebarRight.style.right = `-${sidebarWidth}`;
            sideAtiva = 'left'
        }
    }
}