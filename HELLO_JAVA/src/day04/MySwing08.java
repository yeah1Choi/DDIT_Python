package day04;

import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JLabel;
import javax.swing.JTextField;
import javax.swing.JButton;
import javax.swing.JTextArea;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;

public class MySwing08 extends JFrame {

	private JPanel contentPane;
	private JTextField tf_first;
	private JTextField tf_last;
	JTextArea ta;
	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					MySwing08 frame = new MySwing08();
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
	public MySwing08() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 307, 498);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));

		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		JLabel lbl_first = new JLabel("첫별수:");
		lbl_first.setBounds(52, 35, 57, 15);
		contentPane.add(lbl_first);
		
		JLabel lbl_last = new JLabel("끝별수:");
		lbl_last.setBounds(52, 77, 57, 15);
		contentPane.add(lbl_last);
		
		tf_first = new JTextField();
		tf_first.setBounds(121, 32, 116, 21);
		contentPane.add(tf_first);
		tf_first.setColumns(10);
		
		tf_last = new JTextField();
		tf_last.setColumns(10);
		tf_last.setBounds(121, 74, 116, 21);
		contentPane.add(tf_last);
		
		JButton btn = new JButton("별피라미드");
		btn.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				myClick();
			}
		});
		btn.setBounds(52, 122, 185, 23);
		contentPane.add(btn);
		
		ta = new JTextArea();
		ta.setBounds(36, 171, 216, 263);
		contentPane.add(ta);
	}
	String getStar(int cnt) {
		String ret = "";
		for(int i=0;i<cnt;i++) {
			ret += "🌸";
		}
		return ret;
	}
	
	void myClick() {
		int first = Integer.parseInt(tf_first.getText());
		int last = Integer.parseInt(tf_last.getText());
		
		String txt = "";
		for(int i = first; i <= last; i++) {
				txt += getStar(i)+"\n"; 
		}
		ta.setText(txt);
	}
}
