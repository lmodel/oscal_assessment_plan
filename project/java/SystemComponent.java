package None;

/* metamodel_version: 1.7.0 */
import java.util.List;
import lombok.*;

/**
  A defined component that can be part of an implemented system.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class SystemComponent  {

  private String uuid;
  private String type;
  private String title;
  private String description;
  private String purpose;
  private List<Protocol> protocols;
  private ComponentStatus status;
  private String remarks;
  private List<ResponsibleRole> responsible-roles;
  private List<Property> props;
  private List<Link> links;

}