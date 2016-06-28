<?
switch($_GET['name'])
{
    case 'Annie':
        header('Location: http://localhost:5000/376');
        break;
    case 'Smol':
        header('Location: http://localhost:5000/673');
        break;
    default:
        print "<p>Wrong code. Try again</p>";
        include('index.html');
        break;
}
?>