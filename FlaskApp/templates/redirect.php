<?php
echo "test";
switch($_GET['name'])
{
    case 'Derp':
        header('Location: http://localhost:5000/name/Annie');
        die();
        break;
    case 'Smol':
        header('Location: http://localhost:5000/name/Santiago');
        die();
        break;
    default:
        print "<p>Wrong code. Try again</p>";
        include('index.html');
        break;
}
?>