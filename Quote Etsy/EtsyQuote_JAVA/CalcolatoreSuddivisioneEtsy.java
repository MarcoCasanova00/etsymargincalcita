import javax.swing.*;

public class CalcolatoreSuddivisioneEtsy extends JFrame {
    private JTextField txtEtsy;
    private JTextField txtMarco;
    private JTextField txtDanilo;
    private JButton btnCalcola;
    private JLabel lblMarco;
    private JLabel lblDanilo;

    public CalcolatoreSuddivisioneEtsy() {
        setTitle("Calcolatore Suddivisione Etsy");
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setSize(300, 200);
        setLocationRelativeTo(null);
        setLayout(new BoxLayout(getContentPane(), BoxLayout.Y_AXIS));

        JLabel lblEtsy = new JLabel("Importo Bonifico Etsy:");
        txtEtsy = new JTextField(10);

        JLabel lblAnticipioMarco = new JLabel("Importo Anticipato da Marco:");
        txtMarco = new JTextField(10);

        JLabel lblAnticipioDanilo = new JLabel("Importo Anticipato da Danilo:");
        txtDanilo = new JTextField(10);

        btnCalcola = new JButton("Calcola");
        btnCalcola.addActionListener(e -> calcolaSuddivisione());

        lblMarco = new JLabel("Marco:");
        lblDanilo = new JLabel("Danilo:");

        add(lblEtsy);
        add(txtEtsy);
        add(lblAnticipioMarco);
        add(txtMarco);
        add(lblAnticipioDanilo);
        add(txtDanilo);
        add(btnCalcola);
        add(lblMarco);
        add(lblDanilo);

        setVisible(true);
    }

    private void calcolaSuddivisione() {
        double bonificoEtsy = Double.parseDouble(txtEtsy.getText());
        double anticipioMarco = Double.parseDouble(txtMarco.getText());
        double anticipioDanilo = Double.parseDouble(txtDanilo.getText());

        double metaBonifico = bonificoEtsy / 2;

        double quotaMarco = metaBonifico - (anticipioDanilo - anticipioMarco) / 2;
        double quotaDanilo = metaBonifico + (anticipioDanilo - anticipioMarco) / 2;

        lblMarco.setText("Marco: " + String.format("%.2f", quotaMarco));
        lblDanilo.setText("Danilo: " + String.format("%.2f", quotaDanilo));
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(CalcolatoreSuddivisioneEtsy::new);
    }
}
