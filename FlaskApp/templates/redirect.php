<?php
switch($_GET['mytext'])
{
    case 'Derp':
        header('Location: http://localhost:5000/Annie');
        break;
    case 'Smol':
        header('Location: http://localhost:5000/Santiago');
        break;
    default:
        print "<p>Wrong code. Try again</p>";
        include('index.html');
        break;
}
?>