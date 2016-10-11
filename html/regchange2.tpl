<?xml version="1.0" encoding="ISO-8859-1"?>

<html xmlns="http://www.w3.org/1999/xhtml">
  <head><link rel="shortcut icon" href="favicon.ico" />
    <meta http-equiv="Content-Type" content="text/html; charset=ISO-8859-1" />
    <meta http-equiv="Expires" content="now" />
    <meta http-equiv="Cache-Control" content="no-cache" />
    <meta http-equiv="Pragma" content="no-cache" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />

    <link href="OKUSON.css" type="text/css" rel="StyleSheet" />

    <title>�nderung von Daten</title>
  </head>

  <body>
    <Header />
    <h1>�nderung von Daten</h1>

    <h2>Vorlesung: <CourseName />, <Semester />, <Lecturer /></h2>

<p>Wir haben die folgenden Daten zur Verwaltung des �bungsbetriebes und
zu statistischen Zwecken gespeichert. Hier k�nnen Sie �nderungen
vornehmen. Vergessen Sie bitte nicht, vor dem Abschicken Ihr
Passwort einzugeben! Wenn Sie Ihr Passwort �ndern wollen, dann geben
Sie bitte unten einmal das alte und zweimal das neue ein. Lassen
Sie die beiden Felder f�r das neue Passwort einfach leer, wenn Sie
Ihr Passwort nicht �ndern wollen.
</p>

<form action="SubmitRegChange" method="post">
  <table class="regdata">
    <tr>
      <td> <strong>Notwendige Angaben:</strong> </td>
      <td></td>
    </tr>

    <tr>
      <td>Matrikelnummer:</td>
      <td> <HiddenIdField /> </td>
    </tr>

    <tr>
      <td>Nachname:</td>
      <td> <LastNameField /> </td>
    </tr>

    <tr>
      <td>Vorname:</td>
      <td> <FirstNameField /> </td>
    </tr>

    <tr>
      <td>Studiengang:</td>
      <td> <select name="stud">
             <PossibleStudies />
           </select>
        <TopicField />
        (falls "Sonstiges:").
      </td>
    </tr>

    <tr>
      <td>Fachsemester:</td>
      <td> <SemesterField /> </td>
    </tr>

    <!-- The following should be activated if you allow participants to
         change their tutoring group number (see <GroupChangePossible> in
         Config.xml . -->
    <!--
    <tr>
      <td>�bungsgruppennummer:</td>
      <td> <GroupField /> </td>
    </tr>
    -->

    <tr>
      <td>Neues Passwort (<a href="hinwpasswd.html">HINWEIS</a>):</td>
      <td> <input type="password" class="short" maxlength="16" name="pw1"
        value="" />
      </td>
    </tr>

    <tr>
      <td>Neues Passwort nochmal:</td>
      <td> <input type="password" class="short" maxlength="16" name="pw2"
        value="" />
      </td>
    </tr>

    <tr>
      <td> <strong>Freiwillige Angaben:</strong> </td>
      <td></td>
    </tr>

    <tr>
      <td>Email:</td>
      <td> <EmailField /> </td>
    </tr>

    <tr>
      <td>Einteilungswunsch:</td>
      <td> <WishesField /> </td>
    </tr>

    <tr>
      <td>Passwort: <input type="password" class="short" maxlength="16" 
                           name="passwd" value="" /></td>
      <td> <input type="submit" name="Action" value="Abschicken" /> </td>
    </tr>

  </table>

  <p>Bitte geben Sie unter "Einteilungswunsch" die Matrikelnummern
  der Kommilitoninnen/Kommilitonen ein, mit denen Sie zusammen in eine
  �bungsgruppe eingeteilt werden m�chten. Trennen Sie die Nummern
  durch L�cken oder Kommas.</p>
</form>

    <hr />

    <p><a href="index.html">Zur�ck zur Startseite</a></p>

    <p class="foot">Bei Fragen wenden Sie sich bitte an: <br />
      <Feedback /> 
    </p>

    <p class="foot">
      <ValidatorIcon /> <a href="http://www.math.rwth-aachen.de/~OKUSON/">
      (OKUSON <Version/>)</a>
    </p>
    <Footer />
  </body>
</html>

<!-- Copyright 2003 Frank L�beck and Max Neunh�ffer
      -->

