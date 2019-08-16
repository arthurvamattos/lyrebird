let aberto = false;

const sidebar = document.getElementById('sidebar');
const sidebarRight = document.getElementById('sidebar-right');
const content = document.getElementById('content');

const responsivo = window.innerWidth < 770 ? true : false;

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
            sidebarRight.style.right = '0';
        } else {
            sidebar.style.left = '0';
        }               
        content.style.width = `calc(100% - ${sidebarWidth}`;        
        aberto = true;
    }
}
