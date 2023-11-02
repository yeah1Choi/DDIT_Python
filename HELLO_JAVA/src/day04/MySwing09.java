package day04;

import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JTextField;
import javax.swing.JButton;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;
import java.awt.event.ActionListener;
import java.awt.event.ActionEvent;
import javax.swing.JOptionPane;
import javax.swing.SwingConstants;

public class MySwing09 extends JFrame {

	private JPanel contentPane;
	private JTextField tf;
	String txt = "";
	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					MySwing09 frame = new MySwing09();
					frame.setVisible(true);
				} catch (Exception e) {
					e.printStackTrace();
				}
			}
		});
	}

	/**
	 * Create the frame.
	 */
	public MySwing09() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 244, 262);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));

		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		tf = new JTextField();
		tf.setHorizontalAlignment(SwingConstants.RIGHT);
		tf.setBounds(32, 35, 170, 21);
		contentPane.add(tf);
		tf.setColumns(10);
		
		JButton btn1 = new JButton("1");
		btn1.setBounds(23, 75, 45, 23);
		contentPane.add(btn1);
		
		JButton btn2 = new JButton("2");
		btn2.setBounds(91, 75, 45, 23);
		contentPane.add(btn2);
		
		JButton btn3 = new JButton("3");
		btn3.setBounds(159, 75, 45, 23);
		contentPane.add(btn3);
		
		JButton btn4 = new JButton("4");
		btn4.setBounds(23, 108, 45, 23);
		contentPane.add(btn4);
		
		JButton btn5 = new JButton("5");
		btn5.setBounds(91, 108, 45, 23);
		contentPane.add(btn5);
		
		JButton btn6 = new JButton("6");
		btn6.setBounds(159, 108, 45, 23);
		contentPane.add(btn6);
		
		JButton btn7 = new JButton("7");
		btn7.setBounds(23, 141, 45, 23);
		contentPane.add(btn7);
		
		JButton btn8 = new JButton("8");
		btn8.setBounds(91, 141, 45, 23);
		contentPane.add(btn8);
		
		JButton btn9 = new JButton("9");
		btn9.setBounds(159, 141, 45, 23);
		contentPane.add(btn9);
		
		JButton btn0 = new JButton("0");
		btn0.setBounds(23, 174, 45, 23);
		contentPane.add(btn0);
		
		JButton btn_call = new JButton("☎");
		btn_call.setBounds(85, 174, 117, 23);
		contentPane.add(btn_call);
		
		btn1.addMouseListener(new MouseAdapter() { public void mouseClicked(MouseEvent e) { myclick(e); } });
		btn2.addMouseListener(new MouseAdapter() { public void mouseClicked(MouseEvent e) { myclick(e); } });
		btn3.addMouseListener(new MouseAdapter() { public void mouseClicked(MouseEvent e) { myclick(e); } });
		btn4.addMouseListener(new MouseAdapter() { public void mouseClicked(MouseEvent e) { myclick(e); } });
		btn5.addMouseListener(new MouseAdapter() { public void mouseClicked(MouseEvent e) { myclick(e); } });
		btn6.addMouseListener(new MouseAdapter() { public void mouseClicked(MouseEvent e) { myclick(e); } });
		btn7.addMouseListener(new MouseAdapter() { public void mouseClicked(MouseEvent e) { myclick(e); } });
		btn8.addMouseListener(new MouseAdapter() { public void mouseClicked(MouseEvent e) { myclick(e); } });
		btn9.addMouseListener(new MouseAdapter() { public void mouseClicked(MouseEvent e) { myclick(e); } });
		btn0.addMouseListener(new MouseAdapter() { public void mouseClicked(MouseEvent e) { myclick(e); } });
		
		btn_call.addMouseListener(new MouseAdapter() { public void mouseClicked(MouseEvent e) { myCall(); } });
	}
	void myclick(MouseEvent e) {
		JButton temp = (JButton) e.getComponent();
		String str_new = temp.getText();
		String str_old = tf.getText();
		
		tf.setText(str_old+str_new);
	}
	
	void myCall() {
		String str_tel = tf.getText();
		
		JOptionPane.showMessageDialog(null, "calling to "+str_tel);
	}
}
