<?xml version="1.0" encoding="ISO-8859-1"?>

<html xmlns="http://www.w3.org/1999/xhtml">
  <head>
    <meta http-equiv="Content-Type" content="text/html; charset=ISO-8859-1" />
    <meta http-equiv="Expires" content="now" />
    <meta http-equiv="Cache-Control" content="no-cache" />
    <meta http-equiv="Pragma" content="no-cache" />

    <link href="/OKUSON.css" type="text/css" rel="StyleSheet" />

    <title>�bungsblatt abrufen</title>
  </head>

  <body>
    <h1>�bungsblatt abrufen</h1>

    <h2>Vorlesung: <CourseName />, <Semester />, <Lecturer /></h2>

    <IfIndividualSheets>
    <p>Bitte geben Sie Ihre Matrikelnummer und Ihr Passwort ein (mit dem
    Sie sich <a href="/registration.html">angemeldet</a> haben).
    </p>
    </IfIndividualSheets>

<!--    <p>Auch wenn Sie nicht angemeldet sind, k�nnen Sie sich als Gast
    Beispielbl�tter ansehen. Benutzen Sie die Nummer <GuestId />
    mit beliebigem (auch leerem) Passwort.</p>
-->
    <form action="QuerySheet" method="post">

    <table>
    <IfIndividualSheets>
    <tr><td>Ihre Matrikelnummer: </td>
    <td><input size="8"  maxlength="6" name="id" value="" 
               tabindex="1"/></td></tr>
    <tr><td>Ihr Passwort: </td>
    <td><input type="password" size="16"
               maxlength="16" name="passwd" value="" tabindex="2" /> </td></tr>
    </IfIndividualSheets>
    <tr><td>Gew�nschter Dokumenttyp 
            (<a href="/doctypehelp.html">Hilfe</a>):</td>
    <td><select name="format" tabindex="10000">
    <IfIndividualSheets>
        <option selected="selected">HTML</option>
        <option>PDF</option>
    </IfIndividualSheets>
    <IfNoIndividualSheets>
        <option>HTML</option>
        <option selected="selected">PDF</option>
    </IfNoIndividualSheets>
    </select></td></tr>
    <tr><td>Aufl�sung (HTML):</td>
    <td><select name="resolution" tabindex="10001">
        <AvailableResolutions />
    </select></td></tr>
    </table>

    <p>Die folgenden �bungsbl�tter sind verf�gbar:</p>
    <p><AvailableSheetsAsButtons /></p>

    </form>

    <hr />

    <p><a href="/index.html">Zur�ck zur Startseite</a></p>

    <p class="foot">Bei Fragen wenden Sie sich bitte an: <br />
      <Feedback /> 
    </p>

    <p class="foot">
      <ValidatorIcon />
    </p>
  </body>
</html>

<!-- Copyright 2003 Frank L�beck and Max Neunh�ffer
     $Id: exquery.tpl,v 1.3 2004/03/05 14:31:54 luebeck Exp $ -->

